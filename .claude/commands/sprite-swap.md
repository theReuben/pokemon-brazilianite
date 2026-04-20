# Sprite Swap

Swap all sprites for a given trainer class in pokemon-brazilianite.

## Usage
`/sprite-swap <trainer_name>`

`$ARGUMENTS` contains the trainer name (e.g. `cooltrainer_f`, `brendan`, `algorithm_admin_m`).

---

## Step 1 — Discover existing sprite files

Using the trainer name from `$ARGUMENTS`, check for the following files and directories.
Record exactly which ones exist (use Bash `test -e` or equivalent):

| Slot | Path | Expected format |
|------|------|-----------------|
| **front** | `graphics/trainers/front_pics/<name>.png` | 64×64 4-bit indexed PNG |
| **back** | `graphics/trainers/back_pics/<name>.png` | 64×256 4-bit indexed PNG (4-frame sheet) |
| **palette** | `graphics/trainers/palettes/<name>.pal` | JASC-PAL, exactly 16 colours |
| **overworld (dir)** | `graphics/object_events/pics/people/<name>/` | Directory of action PNGs |
| **overworld (flat)** | `graphics/object_events/pics/people/<name>.png` | Single 144×32 4-bit indexed PNG |

A trainer may have any combination of these. Some trainers (e.g. generic classes) only have a front sprite and palette; playable characters also have a back sprite and a full overworld directory.

If `$ARGUMENTS` is empty or no files are found under any of the five slots, stop and ask the user to confirm the trainer name. List the closest matches by running:
```
ls graphics/trainers/front_pics/ | grep -i "<name>"
ls graphics/object_events/pics/people/ | grep -i "<name>"
```

---

## Step 2 — Report what was found

Print a clear summary table, for example:

```
Sprites found for "cooltrainer_f":
  ✓ front    graphics/trainers/front_pics/cooltrainer_f.png  (64×64, 4-bit indexed)
  ✓ palette  graphics/trainers/palettes/cooltrainer_f.pal    (JASC-PAL, 16 colours)
  ✗ back     (not present — no back sprite for this trainer)
  ✗ overworld (not present — no overworld sprite for this trainer)
```

Use `file <path>` to confirm actual dimensions and mode for each found file.

---

## Step 3 — State compliance requirements

For each slot that **exists**, tell the user exactly what a valid replacement must be:

### front
- PNG file
- Dimensions: **64 × 64 pixels** (must exactly match)
- Colour mode: **4-bit indexed** (max 16 colours, no alpha channel)
- Non-interlaced

### back
- PNG file
- Dimensions: **64 × 256 pixels** (4 frames stacked vertically, each 64×64)
- Colour mode: **4-bit indexed** (max 16 colours, no alpha channel)
- Non-interlaced

### palette
- Plain-text file
- Must begin with `JASC-PAL` on line 1, `0100` on line 2, `16` on line 3
- Exactly **16 RGB colour entries** (lines 4–19), each `R G B` with values 0–255
- Colours should match or complement the replacement front/back sprites

### overworld (flat)
- PNG file
- Dimensions: **144 × 32 pixels** (9 frames × 32 px wide, 1 row of 32 px tall)
- Colour mode: **4-bit indexed** (max 16 colours, no alpha channel)
- Non-interlaced

### overworld (directory)
For each action PNG inside `graphics/object_events/pics/people/<name>/`, a replacement PNG with the **same filename** must be provided. Each replacement must:
- Match the **exact dimensions** of the original file it replaces (run `file <original>` to confirm)
- Be a **4-bit indexed PNG**, non-interlaced

List the required filenames by running `ls graphics/object_events/pics/people/<name>/`.

---

## Step 4 — Request replacement files

Ask the user to provide file paths for each required replacement. Accept them as a space-separated list or one per line. For overworld directories, the user may either:
- Provide a path to a **replacement directory** containing all action PNGs, or
- Provide individual file paths in the format `<action>=<path>` (e.g. `walking=/tmp/new_walking.png`)

Do not proceed until the user has supplied a path for every slot that exists.

---

## Step 5 — Validate each replacement

Before overwriting anything, validate every supplied replacement file:

1. **File exists** — `test -f <path>` or equivalent.
2. **Correct extension** — `.png` for sprites, `.pal` for palettes.
3. **Dimensions and mode** — run `file <path>` and parse the output. Compare against the required values from Step 3. Reject and report any mismatch.
4. **Palette file format** — read the first 3 lines and confirm `JASC-PAL / 0100 / 16`. Count the colour entries; must be exactly 16.
5. **Overworld directory** — verify every required action filename is present in the provided directory.

If any validation fails, report the specific problem(s) and ask the user to supply a corrected file. Do **not** proceed with a partial swap that leaves inconsistent state.

---

## Step 6 — Perform the swap

Once all validations pass:

1. For each slot, copy the validated replacement over the original path (use `cp`).
2. For an overworld directory, copy each action PNG individually into `graphics/object_events/pics/people/<name>/`.
3. After copying, re-run `file <destination>` on each replaced file to confirm the copy succeeded.

---

## Step 7 — Confirm and summarise

Print a final summary of every file that was replaced, e.g.:

```
Sprite swap complete for "cooltrainer_f":
  ✓ graphics/trainers/front_pics/cooltrainer_f.png  → replaced
  ✓ graphics/trainers/palettes/cooltrainer_f.pal    → replaced
```

Remind the user that the ROM must be recompiled (`make`) for the changes to take effect.
