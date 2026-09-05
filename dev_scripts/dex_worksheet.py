#!/usr/bin/env python3
"""Maintain rom_hack_docs/dex_changes.md - a working list of the regional dex.

Reads the species table straight out of src/data/pokemon/species_info/ so the
typing and base stats shown are whatever the game currently builds with.

    python3 dev_scripts/dex_worksheet.py --diff    what the file asks to change
    python3 dev_scripts/dex_worksheet.py           rebuild it from game data
    python3 dev_scripts/dex_worksheet.py --force   rebuild, discarding edits

The worksheet can be edited two ways: by writing in the Changes column, or by
typing over the Type and stat cells directly. --diff reports both. A plain
rebuild refuses to run while direct edits are pending, so a regenerate can't
throw away work that hasn't been applied yet.
"""

import re, glob, os, sys

OUT = 'rom_hack_docs/dex_changes.md'
GEN = {f'GEN_{i+1}': i for i in range(9)}
GEN['GEN_LATEST'] = 8
CONF = {'P_UPDATED_STATS': 8, 'P_UPDATED_TYPES': 8, 'P_UPDATED_ABILITIES': 8}

# Species whose dex name doesn't map straight onto a SPECIES_ constant,
# usually because the base name is a form container rather than a real entry.
MANUAL = {
    'Toxtricity':       'SPECIES_TOXTRICITY_AMPED',
    'Meowstic':         'SPECIES_MEOWSTIC_M',
    'Gimmighoul':       'SPECIES_GIMMIGHOUL_CHEST',
    'Castform':         'SPECIES_CASTFORM_NORMAL',
    'Hisuian Basculin': 'SPECIES_BASCULIN_WHITE_STRIPED',
    'Basculegion':      'SPECIES_BASCULEGION_M',
    'Rotom':            'SPECIES_ROTOM',
}
REGION = {'Alolan': 'ALOLA', 'Galarian': 'GALAR', 'Hisuian': 'HISUI', 'Paldean': 'PALDEA'}


def field(body, name):
    """Text of `.name = ...` up to the comma that closes it, paren/brace aware."""
    m = re.search(r'\.%s\s*=\s*' % name, body)
    if not m:
        return None
    i, depth = m.end(), 0
    for j in range(i, len(body)):
        c = body[j]
        if c in '([{':
            depth += 1
        elif c in ')]}':
            if depth == 0:
                return body[i:j].strip()
            depth -= 1
        elif c == ',' and depth == 0:
            return body[i:j].strip()
    return body[i:].strip()


def resolve(expr):
    """Collapse `P_UPDATED_STATS >= GEN_N ? a : b` chains using the configured gen."""
    if expr is None:
        return None
    e = expr
    while '?' in e:
        m = re.match(r'\s*([A-Z_0-9]+)\s*(>=|<=|==|>|<)\s*([A-Z_0-9]+)\s*\?\s*(.*)$', e, re.S)
        if not m:
            break
        lhs, op, rhs, rest = m.groups()
        l, r = CONF.get(lhs, GEN.get(lhs)), CONF.get(rhs, GEN.get(rhs))
        if l is None or r is None:
            break
        cond = {'>=': l >= r, '<=': l <= r, '==': l == r, '>': l > r, '<': l < r}[op]
        depth, split = 0, None
        for j, c in enumerate(rest):
            if c in '([{':
                depth += 1
            elif c in ')]}':
                depth -= 1
            elif c == ':' and depth == 0:
                split = j
                break
        if split is None:
            break
        e = (rest[:split] if cond else rest[split + 1:]).strip()
    return e.strip()


def load_species():
    files = glob.glob('src/data/pokemon/species_info/*.h')
    macros = {}
    for f in files:
        for m in re.finditer(r'#define\s+([A-Z_0-9]+)\s*(\{[^}]*\})', open(f, encoding='utf-8').read()):
            macros[m.group(1)] = m.group(2)

    out = {}
    for f in files:
        src = open(f, encoding='utf-8').read()
        for m in re.finditer(r'\[(SPECIES_[A-Z0-9_]+)\]\s*=\s*\{', src):
            key, i, depth, j = m.group(1), m.end(), 1, m.end()
            while depth and j < len(src):
                if src[j] == '{':
                    depth += 1
                elif src[j] == '}':
                    depth -= 1
                j += 1
            body = src[i:j]

            t = resolve(field(body, 'types'))
            t = macros.get(t, t)
            if not t:
                continue
            inner = re.search(r'MON_TYPES\(([^)]*)\)', t) or re.search(r'\{([^}]*)\}', t)
            if not inner:
                continue
            types = [x.strip().replace('TYPE_', '').title()
                     for x in inner.group(1).split(',') if x.strip()]

            stats, ok = {}, True
            for k, fld in (('hp', 'baseHP'), ('atk', 'baseAttack'), ('df', 'baseDefense'),
                           ('spa', 'baseSpAttack'), ('spd', 'baseSpDefense'), ('spe', 'baseSpeed')):
                v = resolve(field(body, fld))
                if v is None or not v.isdigit():
                    ok = False
                    break
                stats[k] = int(v)
            if not ok:
                continue

            nm = re.search(r'\.speciesName\s*=\s*_\("([^"]*)"\)', body)
            out[key] = dict(name=nm.group(1) if nm else key, types=types, **stats)
    return out


def read_dex():
    rows = []
    for line in open('rom_hack_docs/regional_dex.md', encoding='utf-8'):
        m = re.match(r'\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|', line)
        if m:
            rows.append((int(m.group(1)), m.group(2).strip(), m.group(4).strip()))
    return rows


def candidates(display):
    d = display.strip()
    if d in MANUAL:
        return [MANUAL[d]]
    suffix = ''
    for word, reg in REGION.items():
        if d.startswith(word + ' '):
            d, suffix = d[len(word) + 1:], '_' + reg
    tight = re.sub(r'[^A-Za-z0-9]', '', d).upper()
    snake = re.sub(r'[^A-Za-z0-9]+', '_', d).upper().strip('_')
    return [f'SPECIES_{b}{suffix}{s}' for b in (tight, snake) for s in ('', '_M', '_NORMAL')]


STAT_KEYS = ('hp', 'atk', 'df', 'spa', 'spd', 'spe')


def read_worksheet():
    """Parse the current worksheet: {dex no: {name, types, stats..., changes}}."""
    rows = {}
    if not os.path.exists(OUT):
        return rows
    for line in open(OUT, encoding='utf-8'):
        c = [x.strip() for x in line.split('|')]
        if len(c) >= 12 and c[1].isdigit():
            try:
                rows[int(c[1])] = dict(
                    name=c[2], types=c[3], changes=c[11],
                    **{k: int(c[4 + i]) for i, k in enumerate(STAT_KEYS)})
            except ValueError:
                pass
    return rows


def existing_notes():
    return {n: r['changes'] for n, r in read_worksheet().items()}


def pending(sp, rows):
    """Rows where the worksheet disagrees with the game data, or has a note."""
    out = []
    for num, name, _ in rows:
        key = next((c for c in candidates(name) if c in sp), None)
        w = read_worksheet().get(num)
        if key is None or w is None:
            continue
        d, edits = sp[key], []
        want = w['types'].replace(' ', '')
        have = '/'.join(d['types'])
        if want and want.lower() != have.lower():
            edits.append('type: %s -> %s' % (have, want))
        for k, label in zip(STAT_KEYS, ('HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe')):
            if w[k] != d[k]:
                edits.append('%s: %d -> %d (%+d)' % (label, d[k], w[k], w[k] - d[k]))
        if edits or w['changes']:
            out.append((num, name, key, edits, w['changes']))
    return out


HEADER = '''# Dex Change Worksheet

Every Pokemon in the regional dex, with the typing and base stats it currently
builds with. Generated from the game data - do not hand-edit anything except the
**Changes** column.

## How to use this

Write what you want changed in the Changes column. Leave it blank for anything
you're happy with. Free text is fine, but these forms are unambiguous:

| To change | Write |
|-----------|-------|
| Typing | `type: Grass/Steel` (or `type: Grass` to make it single) |
| Every base stat | `stats: 80/120/70/60/70/100` (HP/Atk/Def/SpA/SpD/Spe) |
| One base stat | `spe: 110` or `atk: +15` |
| An evolution | `evo: level 32 -> Gyarados` or `evo: Water Stone -> Ludicolo` |
| A learnset | `learn: 25 Flamethrower, 31 Slack Off` |
| Move access | `moves: +Earthquake, -Tackle` |
| An ability | `ability: +Levitate` or `ability: Overgrow / Chlorophyll` |

Several changes for one Pokemon go in the same cell, separated by `;` - for
example `type: Grass/Steel; spe: 110; evo: level 40 -> Torterra`.

Regenerate after edits are applied with `python3 dev_scripts/dex_worksheet.py`;
your Changes column is preserved.

## Forms

Where a dex entry covers a family with several forms, these are the ones the
stats below refer to: Castform (Normal), Rotom (base), Toxtricity (Amped),
Meowstic (Male), Gimmighoul (Chest), Hisuian Basculin (White-Striped),
Basculegion (Male).

## The dex

'''


def main():
    if not os.path.exists('rom_hack_docs/regional_dex.md'):
        sys.exit('run this from the repo root')
    sp, rows, notes = load_species(), read_dex(), existing_notes()
    args = sys.argv[1:]

    if '--diff' in args:
        found = pending(sp, rows)
        if not found:
            print('no changes requested - worksheet matches the game data')
            return
        print('%d Pokemon with requested changes:\n' % len(found))
        for num, name, key, edits, note in found:
            print('%3d  %-20s %s' % (num, name, key))
            for e in edits:
                print('       edited cell  %s' % e)
            if note:
                print('       note         %s' % note)
        return

    stale = [f for f in pending(sp, rows) if f[3]]
    if stale and '--force' not in args:
        sys.exit('%d Pokemon have edited Type/stat cells that are not in the game data yet.\n'
                 'Rebuilding now would discard them. Run with --diff to see them, '
                 'or --force to rebuild anyway.' % len(stale))

    lines = [HEADER,
             '| #   | Pokemon             | Type              | HP  | Atk | Def | SpA | SpD | Spe | BST | Changes |',
             '|-----|---------------------|-------------------|-----|-----|-----|-----|-----|-----|-----|---------|']
    missing = []
    for num, name, _ in rows:
        key = next((c for c in candidates(name) if c in sp), None)
        if key is None:
            missing.append(name)
            continue
        d = sp[key]
        bst = d['hp'] + d['atk'] + d['df'] + d['spa'] + d['spd'] + d['spe']
        lines.append('| %-3d | %-19s | %-17s | %-3d | %-3d | %-3d | %-3d | %-3d | %-3d | %-3d | %s |' % (
            num, name, '/'.join(d['types']), d['hp'], d['atk'], d['df'],
            d['spa'], d['spd'], d['spe'], bst, notes.get(num, '')))

    open(OUT, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    print('wrote %s  (%d Pokemon, %d notes carried over)' % (OUT, len(rows) - len(missing), sum(1 for v in notes.values() if v)))
    if missing:
        print('could not match: ' + ', '.join(missing))


if __name__ == '__main__':
    main()
