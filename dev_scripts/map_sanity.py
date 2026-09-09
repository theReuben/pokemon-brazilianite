#!/usr/bin/env python3
"""Sanity checks for the map data, aimed at the bugs that hide until late.

    python3 dev_scripts/map_sanity.py

Three checks, each derived from a bug a player actually hit:

  warps      Every warp points at a map that exists, with a warp id that map
             has. A typo here strands the player.
  frlg       No Emerald-side script or map warps into a FireRed map. The Safari
             Zone exit did exactly this - it warped to Fuchsia's entrance, a map
             this game never visits - because it was guarded by #ifdef IS_FRLG.
  ifdef      No file tests an always-defined macro with #ifdef/#ifndef. IS_FRLG
             is 0 in an Emerald build, not undefined, so #ifdef IS_FRLG is
             always true and assembles the FireRed branch.

Run dev_scripts/layout_warp_check.py alongside this for the fourth case: content
cut into one layout of a map that can swap layouts at runtime.
"""

import json, re, os, glob, sys

def maps():
    out = {}
    for p in sorted(glob.glob('data/maps/*/map.json')):
        m = json.load(open(p))
        m['_path'] = p
        out[m['id']] = m
    return out


def check_warps(M):
    bad = 0
    for m in M.values():
        for i, w in enumerate(m.get('warp_events', [])):
            dest = M.get(w['dest_map'])
            if w['dest_map'] == 'MAP_DYNAMIC':
                continue
            if dest is None:
                print(f'  {m["id"]} warp {i} -> {w["dest_map"]}, which does not exist')
                bad += 1
                continue
            try:
                n = int(w['dest_warp_id'])
            except ValueError:
                continue
            if n >= len(dest.get('warp_events', [])):
                print(f'  {m["id"]} warp {i} -> {w["dest_map"]} id {n}, but that map has '
                      f'{len(dest.get("warp_events", []))} warps')
                bad += 1
    return bad


def strip_frlg_branches(text):
    """Drop the #if IS_FRLG side of each conditional; that half is not assembled."""
    out, skip = [], 0
    for line in text.split('\n'):
        t = line.strip()
        if re.match(r'#\s*if\s+IS_FRLG', t):
            skip = 1
            continue
        if skip and re.match(r'#\s*else', t):
            skip = 0
            continue
        if skip and re.match(r'#\s*endif', t):
            skip = 0
            continue
        if not skip:
            out.append(line)
    return '\n'.join(out)


def check_frlg(M):
    frlg = {i for i, m in M.items() if '_Frlg/' in m['_path']}
    bad = 0
    for i, m in M.items():
        if i in frlg:
            continue
        for w in m.get('warp_events', []):
            if w['dest_map'] in frlg:
                print(f'  {i} warps into {w["dest_map"]}')
                bad += 1
    # Scripts assembled for every build, not just the FireRed one.
    for p in glob.glob('data/scripts/*.inc') + glob.glob('data/maps/*/scripts.inc'):
        if 'Frlg' in p or 'frlg' in p:
            continue
        text = strip_frlg_branches(open(p, encoding='utf-8', errors='ignore').read())
        for name in sorted(set(re.findall(r'\bMAP_[A-Z0-9_]+\b', text))):
            if name in frlg:
                print(f'  {p} names {name}')
                bad += 1
    return bad


def check_ifdef():
    zero = set()
    for f in glob.glob('include/**/*.h', recursive=True):
        src = open(f, encoding='utf-8', errors='ignore').read()
        zero |= set(re.findall(r'#\s*define\s+([A-Z_][A-Z0-9_]*)\s+(?:0|FALSE)\s*$', src, re.M))
    bad = 0
    for root in ('src', 'data', 'include'):
        for f in glob.glob(root + '/**/*.*', recursive=True):
            if not f.endswith(('.c', '.h', '.inc', '.s')):
                continue
            src = open(f, encoding='utf-8', errors='ignore').read()
            for m in re.finditer(r'#\s*(ifdef|ifndef)\s+([A-Z_][A-Z0-9_]*)', src):
                if m.group(2) in zero:
                    print(f'  {f}: #{m.group(1)} {m.group(2)} - defined as 0, so this is always true')
                    bad += 1
    return bad


def main():
    M = maps()
    total = 0
    for name, fn in (('warps', lambda: check_warps(M)),
                     ('frlg', lambda: check_frlg(M)),
                     ('ifdef', check_ifdef)):
        print(f'== {name}')
        n = fn()
        total += n
        if not n:
            print('  clean')
    print(f'{total} problem(s)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
