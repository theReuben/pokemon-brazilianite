#!/usr/bin/env python3
"""
Trainer Editor — select a trainer and edit their team, dialogue, sprite, or battle music.

Usage:
    python3 dev_scripts/trainer_editor.py [TRAINER_ID]
    python3 dev_scripts/trainer_editor.py           # interactive search
"""

import os
import re
import sys
import shutil
import subprocess
import textwrap
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths (all relative to repo root)
# ---------------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent
TRAINERS_PARTY   = REPO / "src/data/trainers.party"
TRAINERS_INC     = REPO / "data/text/trainers.inc"
FRONT_PICS_DIR   = REPO / "graphics/trainers/front_pics"
POKEMON_C        = REPO / "src/pokemon.c"
SONGS_H          = REPO / "include/constants/songs.h"

# ---------------------------------------------------------------------------
# ANSI colours
# ---------------------------------------------------------------------------

def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if sys.stdout.isatty() else text

def bold(t):   return _c("1", t)
def green(t):  return _c("32", t)
def yellow(t): return _c("33", t)
def cyan(t):   return _c("36", t)
def red(t):    return _c("31", t)
def dim(t):    return _c("2", t)

# ---------------------------------------------------------------------------
# Parse trainers.party
# ---------------------------------------------------------------------------

def parse_trainers() -> dict[str, dict]:
    """Return {TRAINER_ID: {header: str, body: str, name: str, pic: str, music: str, line: int}}"""
    text = TRAINERS_PARTY.read_text(encoding="utf-8")
    trainers = {}
    # Each block starts with === TRAINER_XXX ===
    pattern = re.compile(r"^=== (TRAINER_\S+) ===\s*$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    for i, m in enumerate(matches):
        tid = m.group(1)
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end].rstrip()
        line_no = text[:start].count("\n") + 1

        name  = re.search(r"^Name:[ \t]*(.+)$",  block, re.MULTILINE)
        pic   = re.search(r"^Pic:[ \t]*(.+)$",   block, re.MULTILINE)
        music = re.search(r"^Music:[ \t]*(.+)$",  block, re.MULTILINE)

        trainers[tid] = {
            "block": block,
            "line":  line_no,
            "name":  name.group(1).strip()  if name  else "",
            "pic":   pic.group(1).strip()   if pic   else "",
            "music": music.group(1).strip() if music else "",
        }
    return trainers

# ---------------------------------------------------------------------------
# Fuzzy trainer search
# ---------------------------------------------------------------------------

def select_trainer(trainers: dict, query: str = "") -> str | None:
    """Pick a trainer ID interactively. Returns ID or None."""
    ids = sorted(trainers.keys())

    # Filter by query if given
    if query:
        q = query.upper()
        ids = [t for t in ids if q in t or q in trainers[t]["name"].upper()]

    if not ids:
        print(red("No trainers match that query."))
        return None

    # Try fzf first
    if not query and shutil.which("fzf"):
        lines = [f"{tid:<40} {trainers[tid]['name']}" for tid in ids]
        result = subprocess.run(
            ["fzf", "--prompt=Select trainer> ", "--height=40%", "--reverse"],
            input="\n".join(lines), capture_output=True, text=True
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None
        chosen_id = result.stdout.strip().split()[0]
        return chosen_id

    # Simple numbered list
    if len(ids) == 1:
        return ids[0]

    per_page = 30
    page = 0
    while True:
        start = page * per_page
        chunk = ids[start:start + per_page]
        print()
        for i, tid in enumerate(chunk, start=start + 1):
            print(f"  {dim(str(i).rjust(4))}  {tid:<40} {dim(trainers[tid]['name'])}")
        total = len(ids)
        print(f"\n  Showing {start + 1}–{min(start + per_page, total)} of {total}")
        prompt = "  Enter number, partial name/ID to filter, 'n' next, 'p' prev, or q to quit: "
        choice = input(prompt).strip()
        if choice.lower() == "q":
            return None
        if choice.lower() == "n":
            if start + per_page < total:
                page += 1
            continue
        if choice.lower() == "p":
            if page > 0:
                page -= 1
            continue
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < total:
                return ids[idx]
            print(red("  Out of range."))
            continue
        # Re-filter
        q = choice.upper()
        ids = [t for t in sorted(trainers.keys()) if q in t or q in trainers[t]["name"].upper()]
        page = 0
        if not ids:
            print(red("  No matches — resetting to full list."))
            ids = sorted(trainers.keys())

# ---------------------------------------------------------------------------
# Open in editor
# ---------------------------------------------------------------------------

def open_in_editor(path: Path, line: int = 1):
    editor = os.environ.get("EDITOR") or os.environ.get("VISUAL") or "nano"
    # Most editors accept +N for line number
    try:
        subprocess.run([editor, f"+{line}", str(path)])
    except FileNotFoundError:
        print(red(f"Editor '{editor}' not found. Set $EDITOR or $VISUAL."))

# ---------------------------------------------------------------------------
# Sprite conversion
# ---------------------------------------------------------------------------

FRONT_SIZE = (64, 64)
MAX_COLORS = 16

def _pic_name_to_path(pic: str) -> Path | None:
    """Map a Pic: value like 'Hiker' or 'hiker_frlg' to a front_pic PNG path."""
    # The pic value in trainers.party is the trainer class pic name.
    # File naming: title-cased words joined by underscores → snake_case filename
    # e.g. "Hiker" → hiker.png, "Aqua Admin M" → aqua_admin_m.png
    candidate = pic.lower().replace(" ", "_") + ".png"
    p = FRONT_PICS_DIR / candidate
    return p if p.exists() else None

def sprite_info(trainer: dict) -> str:
    pic = trainer["pic"]
    p = _pic_name_to_path(pic)
    if p:
        return f"{cyan(str(p.relative_to(REPO)))}"
    return f"{yellow('(sprite not found for Pic: ' + pic + ')')}"

def convert_and_import_sprite(src_path: Path, dest_path: Path):
    """Convert any image to a 64×64 16-colour indexed PNG and save to dest_path."""
    try:
        from PIL import Image
    except ImportError:
        print(red("Pillow not installed. Run: pip3 install Pillow"))
        return False

    img = Image.open(src_path).convert("RGBA")

    # Resize to 64×64 using nearest-neighbour to preserve pixel art edges
    if img.size != FRONT_SIZE:
        print(yellow(f"  Resizing {img.size} → {FRONT_SIZE}"))
        img = img.resize(FRONT_SIZE, Image.NEAREST)

    # Flatten alpha onto white background before quantising
    bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    img = bg.convert("RGB")

    # Quantise to exactly 16 colours
    quantised = img.quantize(colors=MAX_COLORS, method=Image.Quantize.MEDIANCUT)
    # Pillow's quantize returns P-mode with indices already in 0..colors-1.
    # Pad the stored palette to full 256-entry size (768 values) so the PNG
    # is written correctly, but keep only 16 unique colour slots.
    palette_data = quantised.getpalette()  # always 768 values (256 * 3)
    trimmed = palette_data[:MAX_COLORS * 3] + [0] * (768 - MAX_COLORS * 3)
    quantised.putpalette(trimmed)
    final = quantised

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    final.save(str(dest_path), format="PNG")
    print(green(f"  Saved → {dest_path.relative_to(REPO)}"))
    return True

def import_sprite_flow(trainer: dict):
    pic = trainer["pic"]
    default_dest = _pic_name_to_path(pic)
    if default_dest is None:
        candidate = pic.lower().replace(" ", "_") + ".png"
        default_dest = FRONT_PICS_DIR / candidate

    print(f"\n  Destination: {cyan(str(default_dest.relative_to(REPO)))}")
    src_raw = input("  Path to new sprite image (PNG/JPG/etc.): ").strip().strip('"').strip("'")
    if not src_raw:
        print(dim("  Cancelled."))
        return

    src = Path(src_raw).expanduser()
    if not src.exists():
        print(red(f"  File not found: {src}"))
        return

    override = input(f"  Save as [{default_dest.name}]? Press Enter to confirm or type new filename: ").strip()
    if override:
        dest = FRONT_PICS_DIR / (override if override.endswith(".png") else override + ".png")
    else:
        dest = default_dest

    if dest.exists():
        yn = input(f"  {yellow(str(dest.name))} already exists. Overwrite? [y/N] ").strip().lower()
        if yn != "y":
            print(dim("  Cancelled."))
            return

    convert_and_import_sprite(src, dest)
    print(f"\n  {dim('Tip: rebuild with')} make {dim('to compile the new sprite.')}")

# ---------------------------------------------------------------------------
# Dialogue search
# ---------------------------------------------------------------------------

def find_dialogue(trainer_name: str) -> list[tuple[Path, int, str]]:
    """Search text files for lines mentioning the trainer name. Returns [(path, lineno, line)]."""
    if not trainer_name:
        return []
    results = []
    text_dirs = [REPO / "data/text", REPO / "asm/scripts"]
    pattern = re.compile(re.escape(trainer_name), re.IGNORECASE)
    for d in text_dirs:
        if not d.exists():
            continue
        for f in sorted(d.rglob("*.inc")):
            for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if pattern.search(line):
                    results.append((f, i, line.strip()))
    return results

# ---------------------------------------------------------------------------
# Battle music
# ---------------------------------------------------------------------------

def load_battle_music_constants() -> dict[str, int]:
    """Return {MUS_VS_*: value} from songs.h."""
    consts = {}
    if not SONGS_H.exists():
        return consts
    for line in SONGS_H.read_text().splitlines():
        m = re.match(r"^\s*#define\s+(MUS_(?:VS|RG_VS)_\S+)\s+(\d+)", line)
        if m:
            consts[m.group(1)] = int(m.group(2))
    return consts

def get_current_custom_music(trainer_id: str) -> str | None:
    """Check if GetBattleBGM in pokemon.c already has a custom override for this trainer."""
    text = POKEMON_C.read_text(encoding="utf-8")
    # Look for a block we'd have inserted
    pattern = re.compile(
        r"// CUSTOM_BATTLE_MUSIC_START:" + re.escape(trainer_id) + r"\s*\n"
        r".*?return (MUS_\S+);.*?"
        r"// CUSTOM_BATTLE_MUSIC_END:" + re.escape(trainer_id),
        re.DOTALL
    )
    m = pattern.search(text)
    return m.group(1) if m else None

def set_battle_music(trainer_id: str, song_const: str):
    """Inject or update a custom battle BGM override for trainer_id in GetBattleBGM()."""
    text = POKEMON_C.read_text(encoding="utf-8")

    start_tag = f"// CUSTOM_BATTLE_MUSIC_START:{trainer_id}"
    end_tag   = f"// CUSTOM_BATTLE_MUSIC_END:{trainer_id}"
    new_block = (
        f"    {start_tag}\n"
        f"    if (SanitizeTrainerId(TRAINER_BATTLE_PARAM.opponentA) == {trainer_id})\n"
        f"        return {song_const};\n"
        f"    {end_tag}\n"
    )

    # If block already exists, replace it
    existing = re.compile(
        r"    // CUSTOM_BATTLE_MUSIC_START:" + re.escape(trainer_id) + r"\n"
        r".*?"
        r"    // CUSTOM_BATTLE_MUSIC_END:" + re.escape(trainer_id) + r"\n",
        re.DOTALL
    )
    if existing.search(text):
        text = existing.sub(new_block, text)
        POKEMON_C.write_text(text, encoding="utf-8")
        print(green(f"  Updated custom battle music for {trainer_id} → {song_const}"))
        return

    # Otherwise insert just before the trainer-class switch in GetBattleBGM
    # Find "else if (gBattleTypeFlags & BATTLE_TYPE_TRAINER)" block → insert before the class switch
    anchor = "        switch (trainerClass)\n        {"
    if anchor not in text:
        print(red("  Could not find insertion point in GetBattleBGM(). Manual edit needed."))
        print(f"  Add this before the 'switch (trainerClass)' in src/pokemon.c:\n")
        print(new_block)
        return

    text = text.replace(anchor, new_block + "        " + anchor.lstrip(), 1)
    POKEMON_C.write_text(text, encoding="utf-8")
    print(green(f"  Set custom battle music for {trainer_id} → {song_const}"))
    print(dim("  Rebuild required: make"))

def remove_battle_music(trainer_id: str):
    text = POKEMON_C.read_text(encoding="utf-8")
    existing = re.compile(
        r"    // CUSTOM_BATTLE_MUSIC_START:" + re.escape(trainer_id) + r"\n"
        r".*?"
        r"    // CUSTOM_BATTLE_MUSIC_END:" + re.escape(trainer_id) + r"\n",
        re.DOTALL
    )
    if not existing.search(text):
        print(yellow("  No custom battle music found for this trainer."))
        return
    text = existing.sub("", text)
    POKEMON_C.write_text(text, encoding="utf-8")
    print(green(f"  Removed custom battle music for {trainer_id}."))

def battle_music_flow(trainer_id: str):
    consts = load_battle_music_constants()
    current = get_current_custom_music(trainer_id)

    print(f"\n  Current custom battle BGM: {cyan(current) if current else dim('(none — uses trainer class default)')}")
    print(f"\n  Available MUS_VS_* constants:")
    for k, v in sorted(consts.items(), key=lambda x: x[1]):
        marker = green(" ← current") if k == current else ""
        print(f"    {k:<35} {dim(str(v))}{marker}")

    print()
    choice = input("  Enter constant name (or 'remove' to clear, Enter to cancel): ").strip()
    if not choice:
        print(dim("  Cancelled."))
        return
    if choice.lower() == "remove":
        remove_battle_music(trainer_id)
        return
    if choice not in consts:
        # Try case-insensitive
        matches = [k for k in consts if k.upper() == choice.upper()]
        if matches:
            choice = matches[0]
        else:
            print(red(f"  '{choice}' not found in songs.h constants."))
            return
    set_battle_music(trainer_id, choice)

# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

def print_trainer_summary(tid: str, t: dict):
    print()
    print(bold(f"  {tid}"))
    print(f"  Name   : {t['name']}")
    print(f"  Pic    : {t['pic']}  →  {sprite_info(t)}")
    print(f"  Music  : {t['music'] or dim('(not set)')}")
    custom_bgm = get_current_custom_music(tid)
    if custom_bgm:
        print(f"  Battle BGM (custom): {cyan(custom_bgm)}")
    print(f"  Party file line: {dim(str(t['line']))}")
    # Show party pokemon — they appear after the first blank line in the block
    _HEADER_KEYS = {"Name:", "Class:", "Pic:", "Gender:", "Music:", "Items:", "Battle",
                    "AI:", "Mugshot", "Starting", "Difficulty:", "Party", "===", "/*", "//"}
    _MON_FIELD   = re.compile(r"^(Level|IVs|EVs|Ability|Nature|Held Item|Ball|Happiness|"
                               r"Shiny|Dynamax|Gigantamax|Tera|-):", re.IGNORECASE)
    after_blank = False
    mons = []
    for line in t["block"].splitlines():
        stripped = line.strip()
        if not after_blank:
            if stripped == "":
                after_blank = True
            continue
        if stripped == "" or stripped.startswith("-") or _MON_FIELD.match(stripped):
            continue
        if any(stripped.startswith(k) for k in _HEADER_KEYS):
            continue
        mons.append(stripped)
    if mons:
        print(f"  Party  :")
        for mon in mons[:6]:
            print(f"           {mon}")

def trainer_menu(tid: str, t: dict):
    while True:
        print_trainer_summary(tid, t)
        print()
        print(f"  {bold('[1]')} Edit team (opens trainers.party at trainer block)")
        print(f"  {bold('[2]')} Edit dialogue (search text files for trainer name)")
        print(f"  {bold('[3]')} Import/convert sprite")
        print(f"  {bold('[4]')} Set custom battle music")
        print(f"  {bold('[b]')} Back to trainer search")
        print(f"  {bold('[q]')} Quit")
        print()
        choice = input("  Choice: ").strip().lower()

        if choice == "1":
            print(f"\n  Opening {TRAINERS_PARTY.relative_to(REPO)} at line {t['line']}…")
            open_in_editor(TRAINERS_PARTY, t["line"])
        elif choice == "2":
            name = t["name"]
            if not name:
                print(yellow("  Trainer has no Name — can't search dialogue."))
                input("  Press Enter to continue…")
                continue
            print(f"\n  Searching for '{name}' in text files…")
            hits = find_dialogue(name)
            if not hits:
                print(yellow(f"  No matches found for '{name}'."))
            else:
                for path, lineno, line in hits[:20]:
                    print(f"  {cyan(str(path.relative_to(REPO)))}:{lineno}  {dim(line[:80])}")
                if len(hits) > 20:
                    print(dim(f"  … and {len(hits) - 20} more"))
                print()
                choice2 = input("  Open a file? Enter file path (or Enter to skip): ").strip()
                if choice2:
                    p = Path(choice2) if choice2.startswith("/") else REPO / choice2
                    # find line in results
                    ln = next((ln for (fp, ln, _) in hits if str(fp).endswith(choice2.lstrip("/"))), 1)
                    open_in_editor(p, ln)
        elif choice == "3":
            import_sprite_flow(t)
            input("\n  Press Enter to continue…")
        elif choice == "4":
            battle_music_flow(tid)
            input("\n  Press Enter to continue…")
        elif choice in ("b", "back"):
            return
        elif choice in ("q", "quit"):
            sys.exit(0)
        else:
            print(red("  Unknown choice."))

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    trainers = parse_trainers()
    print(bold(f"\n  Trainer Editor  —  {len(trainers)} trainers loaded"))
    print(dim(f"  Repo: {REPO}"))

    initial_query = sys.argv[1] if len(sys.argv) > 1 else ""

    while True:
        if initial_query:
            # If exact match, skip search
            if initial_query.upper() in trainers:
                tid = initial_query.upper()
            else:
                tid = select_trainer(trainers, initial_query)
            initial_query = ""
        else:
            tid = select_trainer(trainers)

        if tid is None:
            print(dim("\n  Bye."))
            break

        if tid not in trainers:
            print(red(f"  '{tid}' not found."))
            continue

        trainer_menu(tid, trainers[tid])
        # After returning from menu, reload trainers.party in case user edited it
        trainers = parse_trainers()

if __name__ == "__main__":
    main()
