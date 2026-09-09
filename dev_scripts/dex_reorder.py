#!/usr/bin/env python3
"""Reorder the middle of rom_hack_docs/regional_dex.md by when you can catch things.

Starters stay at the front and the legendary/paradox block stays at the back;
everything between them is sorted into roughly the order the player meets it.

    python3 dev_scripts/dex_reorder.py          rewrite the table
    python3 dev_scripts/dex_reorder.py --dry    print the new order only

Availability is scored as the lowest level the player can first get a species
at, since encounter levels track story progress closely. Sources that need a
tool the player doesn't start with cost a few levels on top - you can't surf,
smash rocks or fish on route 104 the first time through.

Families move as a block, ordered by their earliest member and kept in
evolution order inside the block, so a line is never split across the dex.
"""

import re, os, sys, json, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dex_worksheet import read_dex, candidates, field
from obtainable import species_blocks, frlg_maps, POSTGAME_MAPS, POSTGAME_SCRIPTS
from regional_dex_gen import species_constants, national_nums

DEX = 'rom_hack_docs/regional_dex.md'
# What a source costs on top of its level, for the tool it needs first.
TOLL = {'land_mons': 0, 'rock_smash_mons': 5, 'water_mons': 5, 'fishing_mons': 3}
LATE = 999


def wild_levels():
    """SPECIES_X -> lowest effective level it can be caught at in the wild."""
    skip, out = frlg_maps() | set(POSTGAME_MAPS), {}
    for grp in json.load(open('src/data/wild_encounters.json'))['wild_encounter_groups']:
        if not grp.get('for_maps', True):
            continue
        for enc in grp.get('encounters', []):
            if enc.get('map', '') in skip:
                continue
            for kind, v in enc.items():
                if not isinstance(v, dict) or 'mons' not in v:
                    continue
                for mon in v['mons']:
                    lvl = mon['min_level'] + TOLL.get(kind, 0)
                    sp = mon['species']
                    out[sp] = min(out.get(sp, LATE), lvl)
    return out


def script_levels():
    """SPECIES_X -> level of the earliest gift or static that hands it over."""
    out = {}
    for path in glob.glob('data/**/*.inc', recursive=True):
        name = os.path.basename(os.path.dirname(path))
        if path.startswith('data/scripts/'):
            name = os.path.basename(path)[:-4]
        if '_Frlg' in path or name in POSTGAME_SCRIPTS:
            continue
        for line in open(path, encoding='utf-8', errors='ignore'):
            m = re.match(r'\s*(givemon|setwildbattle)\s+(SPECIES_[A-Z0-9_]+),\s*(\d+)', line)
            if m:
                sp, lvl = m.group(2), int(m.group(3))
                out[sp] = min(out.get(sp, LATE), lvl)
            m = re.match(r'\s*giveegg\s+(SPECIES_[A-Z0-9_]+)', line)
            if m:
                out[m.group(1)] = min(out.get(m.group(1), LATE), 5)
    return out


def main():
    consts, nat, blocks = species_constants(), national_nums(), species_blocks()
    rows = list(read_dex())                             # (num, name, note)
    species_of = {name: next((c for c in candidates(name) if c in consts), None)
                  for _, name, _ in rows}

    level = wild_levels()
    for sp, lvl in script_levels().items():
        level[sp] = min(level.get(sp, LATE), lvl)

    # Families: evolution links, plus forms that share a national dex slot.
    evos = {sp: re.findall(r'SPECIES_[A-Z0-9_]+', field(b, 'evolutions') or '')
            for sp, b in blocks.items()}
    mine = [species_of[n] for _, n, _ in rows]
    group = {sp: sp for sp in mine}
    def root(x):
        while group[x] != x:
            x = group[x]
        return x
    def union(a, b):
        group[root(a)] = root(b)
    for sp in mine:
        for t in evos.get(sp, ()):
            if t in group:
                union(sp, t)
    by_slot = collections.defaultdict(list)
    for sp in mine:
        by_slot[nat[sp]].append(sp)
    for shared in by_slot.values():
        for sp in shared[1:]:
            union(sp, shared[0])

    # Depth in the evolution graph, so a family reads base first.
    depth = {sp: 0 for sp in mine}
    for _ in range(3):
        for sp in mine:
            for t in evos.get(sp, ()):
                if t in depth:
                    depth[t] = max(depth[t], depth[sp] + 1)

    # Starters keep the front, the special block keeps the back, in place.
    is_starter = lambda note: note.startswith('Starter')
    special = ('Paradox', 'Beast Den', 'Storm Roost', 'Tapu Grotto', 'Scam Pillar')
    head = [r for r in rows if is_starter(r[2])]
    tail = [r for r in rows if r not in head and r[2].startswith(special)]
    middle = [r for r in rows if r not in head and r not in tail]

    order = {name: i for i, (_, name, _) in enumerate(rows)}
    fams = collections.defaultdict(list)
    for r in middle:
        fams[root(species_of[r[1]])].append(r)
    def when(fam):
        return min(level.get(species_of[r[1]], LATE) for r in fam)
    ranked = sorted(fams.values(), key=lambda f: (when(f), order[f[0][1]]))
    for fam in ranked:
        fam.sort(key=lambda r: (depth[species_of[r[1]]], order[r[1]]))
    middle = [r for fam in ranked for r in fam]

    out = head + middle + tail
    if '--dry' in sys.argv:
        for i, (_, name, _) in enumerate(out, 1):
            print('%3d %-20s %s' % (i, name, level.get(species_of[name], '-')))
        return 0

    text = open(DEX).read().split('\n')
    first = next(i for i, l in enumerate(text) if re.match(r'\|\s*1\s*\|', l))
    last = max(i for i, l in enumerate(text) if l.startswith('|'))
    types = {name: [c.strip() for c in text[first + j].strip('|').split('|')][2]
             for j, (_, name, _) in enumerate(rows)}
    text[first:last + 1] = ['| %-3d | %-18s | %-17s | %-31s |' % (i, name, types[name], note)
                            for i, (_, name, note) in enumerate(out, 1)]
    open(DEX, 'w').write('\n'.join(text))
    print(f'reordered {len(out)} rows: {len(head)} starters, {len(middle)} middle, {len(tail)} special')
    return 0


if __name__ == '__main__':
    sys.exit(main())
