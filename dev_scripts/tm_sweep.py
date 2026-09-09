#!/usr/bin/env python3
"""List where every TM comes from, and flag the ones you can get twice.

    python3 dev_scripts/tm_sweep.py

A TM is a one-off teaching item here, so a TM that is both sold in a shop and
lying in a ball somewhere is a wasted shelf slot: the shop copy is dead money
for anyone who explored. The report groups each TM by how many places give it
and ends with the TMs no source gives at all, which are what a duplicate shop
slot should be spent on.
"""

import re, os, sys, json, glob, collections

MARTS = 'shop'


def sources():
    """ITEM_TM_X -> [(kind, where)]."""
    out = collections.defaultdict(list)

    for path in glob.glob('data/maps/*/map.json'):
        if '_Frlg' in path:
            continue
        where = os.path.basename(os.path.dirname(path))
        for obj in json.load(open(path)).get('object_events', []):
            item = obj.get('trainer_sight_or_berry_tree_id', '')
            if str(item).startswith('ITEM_TM_'):
                out[item].append(('ball', where))

    for path in glob.glob('data/**/*.inc', recursive=True):
        if '_Frlg' in path:
            continue
        where = os.path.basename(os.path.dirname(path))
        if path.startswith('data/scripts/'):
            where = os.path.basename(path)[:-4]
        text = open(path, encoding='utf-8', errors='ignore').read()
        # Mart lists: pokemart <label> ... .2byte ITEM_TM_X
        for m in re.finditer(r'^(\w+):\n((?:\t\.2byte .*\n)+)', text, re.M):
            for item in re.findall(r'ITEM_TM_[A-Z0-9_]+', m.group(2)):
                out[item].append((MARTS, where))
        seen = set()
        for m in re.finditer(r'^\s*(?:giveitem|additem)\s+(ITEM_TM_[A-Z0-9_]+)', text, re.M):
            # A script often gives the same TM from two branches; count it once.
            if m.group(1) not in seen:
                seen.add(m.group(1))
                out[m.group(1)].append(('script', where))

    for path in glob.glob('data/maps/*/scripts.inc'):     # hidden items
        if '_Frlg' in path:
            continue
        where = os.path.basename(os.path.dirname(path))
        for m in re.finditer(r'hiddenitem\s+(ITEM_TM_[A-Z0-9_]+)',
                             open(path, encoding='utf-8', errors='ignore').read()):
            out[m.group(1)].append(('hidden', where))
    return out


def all_tms():
    return sorted(set(re.findall(r'\[(ITEM_TM_(?!CASE)[A-Z0-9_]+)\]\s*=',
                                 open('src/data/items.h', encoding='utf-8').read())))


def main():
    got = sources()
    dupes = {k: v for k, v in got.items() if len(v) > 1}
    print('%d TMs have a source; %d have more than one\n' % (len(got), len(dupes)))
    for item in sorted(dupes):
        kinds = collections.Counter(k for k, _ in dupes[item])
        mark = ' <- shop + elsewhere' if kinds[MARTS] and len(dupes[item]) > kinds[MARTS] else ''
        print('%-24s %s%s' % (item.replace('ITEM_TM_', ''),
                              ', '.join('%s (%s)' % (w, k) for k, w in dupes[item]), mark))
    missing = [t for t in all_tms() if t not in got]
    print('\n%d TMs with no source at all:' % len(missing))
    print('  ' + ', '.join(t.replace('ITEM_TM_', '') for t in missing))
    return 0


if __name__ == '__main__':
    sys.exit(main())
