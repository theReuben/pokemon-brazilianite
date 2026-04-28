#!/usr/bin/env python3
"""
Update trainer parties to use Pokemon from the Brazilianite regional dex.

Run from the repository root:
    python3 dev_scripts/update_trainer_pokemon.py           # dry run
    python3 dev_scripts/update_trainer_pokemon.py --apply   # apply changes

Dry run prints every replacement that would be made without touching any files.
--apply creates .backup files then writes the changes in place.

Note: this script only replaces species names. Abilities, moves, and held items
that are invalid on the new species will need manual review after running.
"""

import re
import os
import sys
import shutil

# ---------------------------------------------------------------------------
# Mapping: old species name (as it appears in the .party file) → new name.
# Regional form targets use Showdown dash notation (e.g. Geodude-Alola).
# Pokémon already in the regional dex are not listed here.
# Groudon and Kyogre are intentionally omitted (left as-is).
# ---------------------------------------------------------------------------
SPECIES_MAP = {
    # ------------------------------------------------------------------
    # Direct regional form swaps
    # ------------------------------------------------------------------
    "Geodude":  "Geodude-Alola",
    "Graveler": "Graveler-Alola",
    "Golem":    "Golem-Alola",
    "Muk":      "Muk-Alola",
    "Slowpoke": "Slowpoke-Galar",
    "Slowbro":  "Slowbro-Galar",
    "Slowking": "Slowking-Galar",
    "Voltorb":  "Voltorb-Hisui",
    "Electrode":"Electrode-Hisui",

    # ------------------------------------------------------------------
    # Hoenn starter lines → regional starter lines
    # ------------------------------------------------------------------
    "Treecko":   "Turtwig",
    "Grovyle":   "Grotle",
    "Torchic":   "Fuecoco",
    "Combusken": "Crocalor",
    "Mudkip":    "Totodile",
    "Marshtomp": "Croconaw",
    "Bulbasaur": "Turtwig",
    "Charmander":"Fuecoco",

    # ------------------------------------------------------------------
    # Fighting types
    # ------------------------------------------------------------------
    "Machop":    "Timburr",
    "Machoke":   "Gurdurr",
    "Machamp":   "Conkeldurr",
    "Makuhita":  "Timburr",
    "Hariyama":  "Conkeldurr",
    "Meditite":  "Clobbopus",
    "Medicham":  "Grapploct",
    "Hitmonchan":"Conkeldurr",
    "Hitmonlee": "Conkeldurr",
    "Hitmontop": "Grapploct",
    "Shroomish": "Timburr",
    "Breloom":   "Conkeldurr",

    # ------------------------------------------------------------------
    # Psychic types
    # ------------------------------------------------------------------
    "Abra":      "Solosis",
    "Kadabra":   "Duosion",
    "Alakazam":  "Reuniclus",
    "Ralts":     "Espurr",
    "Kirlia":    "Meowstic",
    "Gardevoir": "Meowstic",
    "Spoink":    "Solosis",
    "Grumpig":   "Duosion",
    "Drowzee":   "Espurr",
    "Hypno":     "Meowstic",
    "Chimecho":  "Espurr",
    "Natu":      "Espurr",
    "Xatu":      "Meowstic",
    "Wobbuffet": "Reuniclus",
    "Girafarig": "Meowstic",
    "Lunatone":  "Slowpoke-Galar",
    "Solrock":   "Slowpoke-Galar",
    "Baltoy":    "Yamask-Galar",
    "Claydol":   "Runerigus",
    "Staryu":    "Slowpoke-Galar",
    "Starmie":   "Slowbro-Galar",

    # ------------------------------------------------------------------
    # Electric types
    # ------------------------------------------------------------------
    "Electrike": "Elekid",
    "Manectric": "Electivire",
    "Pikachu":   "Voltorb-Hisui",
    "Raichu":    "Electrode-Hisui",
    "Mareep":    "Elekid",
    "Flaaffy":   "Electabuzz",
    "Ampharos":  "Electivire",
    "Magnemite": "Voltorb-Hisui",
    "Magneton":  "Electrode-Hisui",
    "Plusle":    "Toxel",
    "Minun":     "Toxel",
    "Chinchou":  "Toxel",
    "Lanturn":   "Toxtricity",

    # ------------------------------------------------------------------
    # Fire types
    # ------------------------------------------------------------------
    "Numel":    "Magby",
    "Camerupt": "Magmortar",
    "Slugma":   "Pansear",
    "Magcargo": "Simisear",
    "Torkoal":  "Magmortar",
    "Growlithe":"Pansear",
    "Arcanine": "Simisear",
    "Ponyta":   "Fletchling",
    "Rapidash": "Talonflame",
    "Ninetales":"Simisear",
    "Houndour": "Magby",
    "Houndoom": "Magmortar",

    # ------------------------------------------------------------------
    # Normal/Flying birds
    # ------------------------------------------------------------------
    "Wingull":  "Pikipek",
    "Pelipper": "Toucannon",
    "Taillow":  "Fletchling",
    "Swellow":  "Talonflame",
    "Swablu":   "Fletchling",
    "Altaria":  "Noivern",
    "Doduo":    "Pikipek",
    "Dodrio":   "Toucannon",
    "Hoothoot": "Pikipek",
    "Noctowl":  "Toucannon",

    # ------------------------------------------------------------------
    # Dark types
    # ------------------------------------------------------------------
    "Poochyena": "Murkrow",
    "Mightyena": "Honchkrow",
    "Cacturne":  "Lokix",
    "Seedot":    "Whismur",
    "Nuzleaf":   "Loudred",
    "Shiftry":   "Exploud",
    "Sableye":   "Gimmighoul",
    "Absol":     "Honchkrow",

    # ------------------------------------------------------------------
    # Water types
    # ------------------------------------------------------------------
    "Magikarp":  "Feebas",
    "Gyarados":  "Milotic",
    "Goldeen":   "Panpour",
    "Seaking":   "Simipour",
    "Carvanha":  "Basculin-Hisui",
    "Sharpedo":  "Basculegion",
    "Wailmer":   "Spheal",
    "Wailord":   "Walrein",
    "Horsea":    "Panpour",
    "Seadra":    "Simipour",
    "Kingdra":   "Basculegion",
    "Corphish":  "Totodile",
    "Crawdaunt": "Feraligatr",
    "Marill":    "Panpour",
    "Azumarill": "Simipour",
    "Azurill":   "Snubbull",
    "Golduck":   "Politoed",
    "Clamperl":  "Feebas",
    "Luvdisc":   "Feebas",
    "Barboach":  "Basculin-Hisui",
    "Whiscash":  "Clodsire",
    "Lotad":     "Pansage",
    "Lombre":    "Simisage",
    "Ludicolo":  "Simisage",
    "Lapras":    "Walrein",

    # ------------------------------------------------------------------
    # Bug types
    # ------------------------------------------------------------------
    "Wurmple":   "Tarountula",
    "Silcoon":   "Tarountula",
    "Cascoon":   "Tarountula",
    "Beautifly": "Vespiquen",
    "Dustox":    "Spidops",
    "Nincada":   "Grubbin",
    "Ninjask":   "Vikavolt",
    "Surskit":   "Dewpider",
    "Masquerain":"Araquanid",
    "Volbeat":   "Ledyba",
    "Illumise":  "Ledian",
    "Pinsir":    "Vikavolt",
    "Armaldo":   "Barbaracle",

    # ------------------------------------------------------------------
    # Rock / Ground / Steel
    # Aron line → Alolan Geodude line (preserves 3-stage Rock chain)
    # Flygon line → Aegislash line (full line mapping)
    # ------------------------------------------------------------------
    "Aron":    "Geodude-Alola",
    "Lairon":  "Graveler-Alola",
    "Aggron":  "Golem-Alola",
    "Onix":    "Klawf",
    "Steelix": "Orthworm",
    "Skarmory":"Orthworm",
    "Mawile":  "Klefki",
    "Kabuto":  "Binacle",
    "Kabutops":"Barbaracle",
    "Omanyte": "Binacle",
    "Omastar": "Barbaracle",
    "Aerodactyl":"Barbaracle",
    "Rhyhorn": "Hippopotas",
    "Rhydon":  "Hippowdon",
    "Sandshrew":"Hippopotas",
    "Sandslash":"Hippowdon",
    "Trapinch":"Honedge",
    "Vibrava": "Doublade",
    "Flygon":  "Aegislash",

    # ------------------------------------------------------------------
    # Ghost types
    # ------------------------------------------------------------------
    "Shuppet": "Drifloon",
    "Banette": "Drifblim",
    "Duskull": "Gimmighoul",
    "Dusclops":"Yamask-Galar",

    # ------------------------------------------------------------------
    # Poison types
    # ------------------------------------------------------------------
    "Koffing":   "Grimer-Alola",
    "Weezing":   "Muk-Alola",
    "Gulpin":    "Wooper-Paldea",
    "Seviper":   "Glimmet",
    "Tentacool": "Qwilfish-Hisui",
    "Tentacruel":"Overqwil",

    # ------------------------------------------------------------------
    # Normal types
    # ------------------------------------------------------------------
    "Zigzagoon": "Bidoof",
    "Linoone":   "Bibarel",
    "Skitty":    "Meowth",
    "Delcatty":  "Persian",
    "Zangoose":  "Persian",
    "Spinda":    "Castform",
    "Kecleon":   "Castform",
    "Slakoth":   "Teddiursa",
    "Vigoroth":  "Ursaring",
    "Slaking":   "Ursaluna",
    "Chansey":   "Snubbull",
    "Blissey":   "Granbull",
    "Wigglytuff":"Granbull",
    "Kangaskhan":"Ursaring",
    "Tauros":    "Ursaluna",

    # ------------------------------------------------------------------
    # Grass types
    # ------------------------------------------------------------------
    "Oddish":   "Bounsweet",
    "Gloom":    "Steenee",
    "Bellossom":"Tsareena",
    "Vileplume":"Tsareena",
    "Roselia":  "Smoliv",

    # ------------------------------------------------------------------
    # Ice types
    # ------------------------------------------------------------------
    "Glalie": "Vanilluxe",

    # ------------------------------------------------------------------
    # Dragon / Pseudo-legendary
    # ------------------------------------------------------------------
    "Dratini":   "Noibat",
    "Dragonair": "Noivern",
    "Dragonite": "Noivern",
    "Bagon":     "Noibat",
    "Shelgon":   "Noivern",
    "Salamence": "Noivern",
    "Beldum":    "Gimmighoul",
    "Metang":    "Gholdengo",
    "Metagross": "Gholdengo",

    # ------------------------------------------------------------------
    # Zubat line (cave bats → cave bats)
    # ------------------------------------------------------------------
    "Zubat":  "Noibat",
    "Golbat": "Noivern",
    "Crobat": "Noivern",
}

PARTY_FILES = [
    "src/data/trainers.party",
    "src/data/trainers_frlg.party",
    "src/data/battle_partners.party",
]

# Field prefixes that can never be a species line.
FIELD_PREFIXES = (
    "Name:", "Class:", "Pic:", "Gender:", "Music:", "Items:", "Item:",
    "Battle Type:", "Double Battle:", "AI:", "Mugshot:", "Difficulty:",
    "Starting Status:", "Level:", "Ability:", "IVs:", "EVs:", "Ball:",
    "Happiness:", "Nature:", "Shiny:", "Dynamax", "Gigantamax", "Tera ",
    "-", "//",
)


def extract_species(line):
    """Return the species name from a Pokemon species line, or None."""
    stripped = line.strip()
    if not stripped:
        return None
    # Skip SPECIES_ constant form (legacy / edge case)
    if stripped.startswith("SPECIES_"):
        return None
    # Nickname form: "Name (Species) ..."  — species is the paren group that isn't M or F
    for group in re.findall(r'\(([^)]+)\)', stripped):
        if group not in ("M", "F"):
            return group
    # Plain form: species is everything before the first @ or ( or end
    return re.split(r'\s+[@(]', stripped)[0].strip() or None


def replace_species_in_line(line, old_species, new_species):
    """Swap old_species for new_species in a species line, preserving all other content."""
    # Nickname form: replace inside parens
    if f"({old_species})" in line:
        return line.replace(f"({old_species})", f"({new_species})", 1)
    # Plain form: old_species must be at the start of the non-whitespace content
    stripped = line.lstrip()
    indent = line[: len(line) - len(stripped)]
    if stripped.startswith(old_species):
        rest = stripped[len(old_species):]
        # Guard against partial prefix match (e.g. "Geodude" matching "Geodude-Alola")
        if not rest or rest[0] in (" ", "\t", "\n", "\r"):
            return indent + new_species + rest
    return line


def process_file(filepath):
    """Parse filepath and return (output_lines, list_of_changes).

    Each change is (trainer_id, line_number_1based, old_species, new_species).
    When a species is swapped, its move lines are dropped so the engine fills
    in the last 4 level-up moves at that Pokemon's level automatically.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = []
    changes = []

    in_trainer_block = False
    expect_species = False
    clear_moves = False   # True for the remainder of a block whose species was swapped
    current_trainer = "?"

    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Trainer header line
        if stripped.startswith("==="):
            in_trainer_block = True
            expect_species = False
            clear_moves = False
            m = re.search(r"===\s*(\w+)\s*===", stripped)
            current_trainer = m.group(1) if m else "?"
            output_lines.append(line)
            continue

        if not in_trainer_block:
            output_lines.append(line)
            continue

        # Comment lines — pass through without changing state
        if stripped.startswith("/*") or stripped.startswith("*") or stripped.endswith("*/"):
            output_lines.append(line)
            continue

        # Blank line → next non-blank is a species line; reset move-clearing for new block
        if not stripped:
            expect_species = True
            clear_moves = False
            output_lines.append(line)
            continue

        # Drop move lines for a block whose species was just swapped
        if clear_moves and stripped.startswith("- "):
            continue

        # Known field prefix → not a species line
        if any(stripped.startswith(p) for p in FIELD_PREFIXES):
            expect_species = False
            output_lines.append(line)
            continue

        # Everything else after a blank line is a species line
        if expect_species:
            expect_species = False
            species = extract_species(line)
            if species and species in SPECIES_MAP:
                new_species = SPECIES_MAP[species]
                new_line = replace_species_in_line(line, species, new_species)
                changes.append((current_trainer, lineno, species, new_species))
                output_lines.append(new_line)
                clear_moves = True
                continue

        output_lines.append(line)

    return output_lines, changes


def main():
    apply_changes = "--apply" in sys.argv

    if not os.path.exists("Makefile"):
        print("Error: please run this script from the repository root.")
        sys.exit(1)

    total = 0
    results = {}

    for filepath in PARTY_FILES:
        if not os.path.exists(filepath):
            continue
        output_lines, changes = process_file(filepath)
        results[filepath] = (output_lines, changes)
        total += len(changes)

        print(f"\n{'='*60}")
        print(f"{filepath}  ({len(changes)} replacement(s))")
        print(f"{'='*60}")
        for trainer, lineno, old, new in changes:
            print(f"  {lineno:5d}  [{trainer}]  {old} → {new}")

    print(f"\nTotal replacements: {total}")

    if not apply_changes:
        print("\nDry run — no files modified. Pass --apply to apply changes.")
        return

    for filepath, (output_lines, changes) in results.items():
        if not changes:
            continue
        backup = filepath + ".backup"
        if not os.path.exists(backup):
            shutil.copy2(filepath, backup)
            print(f"Backup created: {backup}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(output_lines)
        print(f"Written: {filepath}")

    print("\nDone. Review the changes, then delete the .backup files when satisfied.")
    print("Moves on swapped Pokemon have been cleared — the engine will assign the last 4")
    print("level-up moves at that Pokemon's level automatically.")
    print("Ability and held item fields on changed Pokemon may still need manual review.")


if __name__ == "__main__":
    main()
