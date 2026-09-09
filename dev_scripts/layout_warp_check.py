#!/usr/bin/env python3
"""Check that every warp tile survives its map's alternate layouts.

A map can swap layouts at runtime (setmaplayoutindex), and anything added to
one layout and not the others disappears when the swap happens. That is how
the Storm Roost entrance went missing: the cave mouth was cut into
LAYOUT_ROUTE111 only, so it vanished the moment Mirage Tower crumbled and
Route 111 switched to LAYOUT_ROUTE111_NO_MIRAGE_TOWER.

    python3 dev_scripts/layout_warp_check.py

Prints every warp whose block differs between the layouts its map can use.
Plenty of those are deliberate - Shoal Cave floods, Seafoam currents stop, the
Sky Pillar appears - so each line is a prompt to look, not proof of a bug.
"""

import json, re, os, glob, sys

LAYOUTS = 'data/layouts/layouts.json'


def layouts():
    return {l['id']: l for l in json.load(open(LAYOUTS))['layouts']}


def blocks(layout):
    data = open(layout['blockdata_filepath'], 'rb').read()
    return [int.from_bytes(data[i:i + 2], 'little') for i in range(0, len(data), 2)]


def main():
    L = layouts()
    hits = 0
    for path in sorted(glob.glob('data/maps/*/map.json')):
        m = json.load(open(path))
        script = path.replace('map.json', 'scripts.inc')
        alts = set()
        if os.path.exists(script):
            alts = set(re.findall(r'setmaplayoutindex (LAYOUT_[A-Z0-9_]+)', open(script).read()))
        used = [m['layout']] + sorted(a for a in alts if a != m['layout'] and a in L)
        if len(used) < 2:
            continue
        sizes = {(L[l]['width'], L[l]['height']) for l in used}
        if len(sizes) > 1:
            print(f'{m["id"]}: layouts differ in size, skipped')
            continue
        w = L[used[0]]['width']
        grids = {l: blocks(L[l]) for l in used}
        for warp in m['warp_events']:
            i = warp['y'] * w + warp['x']
            vals = {l: grids[l][i] for l in used}
            if len(set(vals.values())) > 1:
                hits += 1
                print('%s (%d,%d) -> %s' % (m['id'], warp['x'], warp['y'], warp['dest_map']))
                for l, v in vals.items():
                    print('    %-52s %s' % (l, hex(v)))
    print(f'{hits} warp(s) sit on a tile that changes with the layout')
    return 0


if __name__ == '__main__':
    sys.exit(main())
