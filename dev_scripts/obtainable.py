#!/usr/bin/env python3
"""Work out which species the player can actually get before the post-game.

The regional dex should be exactly this set, so this is the thing the dex is
generated from rather than a hand-written list.

    python3 dev_scripts/obtainable.py            summary + the full list
    python3 dev_scripts/obtainable.py --json     machine-readable, for the dex generator

Sources scanned: wild encounter tables, `setwildbattle` statics, `givemon`
gifts, `giveegg` eggs, in-game trades, and the starter #defines. Everything
those can evolve into is obtainable too, and so is anything they can breed
down into, so both closures are applied.

"Before the post-game" means before the Hall of Fame sets FLAG_SYS_GAME_CLEAR.
The maps and scripts that sit behind that flag are listed in POSTGAME below,
each with the gate that puts it there.
"""

import re, os, sys, json, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dex_worksheet import field

INFO = 'src/data/pokemon/species_info'

# Everything here is reachable only after the Hall of Fame.
POSTGAME_MAPS = {
    'MAP_DESERT_UNDERPASS':          'Fossil Maniac only opens the tunnel on FLAG_SYS_GAME_CLEAR',
    'MAP_ARTISAN_CAVE_1F':           'inside the Battle Frontier',
    'MAP_ARTISAN_CAVE_B1F':          'inside the Battle Frontier',
    'MAP_METEOR_FALLS_STEVENS_CAVE': 'Steven only appears on FLAG_SYS_GAME_CLEAR',
    'MAP_MARINE_CAVE_END':           'abnormal weather, post-game only',
    'MAP_TERRA_CAVE_END':            'abnormal weather, post-game only',
}
POSTGAME_SCRIPTS = {
    'MossdeepCity_StevensHouse':        "Steven's note is hidden until FLAG_SYS_GAME_CLEAR",
    'BattleFrontier_OutsideEast':       'Battle Frontier',
    'BattleFrontier_Lounge6':           'Battle Frontier',
    'LittlerootTown_ProfessorBirchsLab': 'Johto starters unlock with the national dex',
    'MarineCave_End':                   'abnormal weather, post-game only',
    'TerraCave_End':                    'abnormal weather, post-game only',
    'debug':                            'debug menu',
    'gift_pichu':                       'Mystery Gift wonder card, not an in-game event',
}
# Reachable, but the door never opens: the Regi chambers need CheckRelicanthWailord
# and neither Relicanth nor Wailord exists anywhere in this hack.
DEAD_TRADES = []   # filled in by collect(): trades asking for a mon you can't get
UNREACHABLE = {
    'SPECIES_REGIROCK': 'Sealed Chamber needs Relicanth + Wailord, neither is obtainable',
    'SPECIES_REGICE':   'Sealed Chamber needs Relicanth + Wailord, neither is obtainable',
    'SPECIES_REGISTEEL': 'Sealed Chamber needs Relicanth + Wailord, neither is obtainable',
}


def species_values():
    raw = dict(re.findall(r'#define\s+(SPECIES_[A-Z0-9_]+)\s+(\S+)',
                          open('include/constants/species.h').read()))
    def val(n):
        v = raw.get(n)
        return None if v is None else (int(v) if v.isdigit() else val(v))
    return {n: val(n) for n in raw}


def species_blocks():
    out = {}
    for f in glob.glob(os.path.join(INFO, '*.h')):
        src = open(f, encoding='utf-8').read()
        for m in re.finditer(r'\n    \[(SPECIES_[A-Z0-9_]+)\]\s*=\s*\{', src):
            depth, i = 1, m.end()
            while depth and i < len(src):
                depth += (src[i] == '{') - (src[i] == '}')
                i += 1
            out[m.group(1)] = src[m.end():i]
    return out


def frlg_maps():
    return {json.load(open(p))['id'] for p in glob.glob('data/maps/*_Frlg/map.json')}


def wild(sources):
    skip = frlg_maps() | set(POSTGAME_MAPS)
    data = json.load(open('src/data/wild_encounters.json'))
    for grp in data['wild_encounter_groups']:
        if not grp.get('for_maps', True):
            continue                          # frontier / pike / pyramid sets
        for enc in grp.get('encounters', []):
            mp = enc.get('map', '')
            if mp in skip:
                continue
            where = mp.replace('MAP_', '').title().replace('_', ' ')
            for v in enc.values():
                if isinstance(v, dict) and 'mons' in v:
                    for mon in v['mons']:
                        sources[mon['species']].add('wild: ' + where)


def scripts(sources):
    verbs = {'givemon': 'gift', 'setwildbattle': 'static', 'giveegg': 'egg'}
    for path in glob.glob('data/**/*.inc', recursive=True):
        name = os.path.basename(os.path.dirname(path))
        if path.startswith('data/scripts/'):
            name = os.path.basename(path)[:-4]
        if '_Frlg' in path or name in POSTGAME_SCRIPTS:
            continue
        for line in open(path, encoding='utf-8', errors='ignore'):
            m = re.match(r'\s*(\w+)\s+(SPECIES_[A-Z0-9_]+)', line)
            if m and m.group(1) in verbs:
                sources[m.group(2)].add('%s: %s' % (verbs[m.group(1)], name))


def offered_trades():
    """[(map, species given, species asked for)] for the reachable trade NPCs.

    A trade is only a source if the player can get the mon it asks for, so the
    species asked for is part of the answer, not just flavour.
    """
    src = open('src/data/trade.h', encoding='utf-8').read()
    deal = {}
    for m in re.finditer(r'\[(INGAME_TRADE_[A-Z0-9_]+)\]\s*=\s*\{(.*?)\n    \},', src, re.S):
        give = re.search(r'\.species\s*=\s*(SPECIES_[A-Z0-9_]+)', m.group(2))
        want = re.search(r'\.requestedSpecies\s*=\s*(SPECIES_[A-Z0-9_]+)', m.group(2))
        if give and want:
            deal[m.group(1)] = (give.group(1), want.group(1))
    out = []
    for path in glob.glob('data/maps/*/scripts.inc'):
        name = os.path.basename(os.path.dirname(path))
        if '_Frlg' in path or name in POSTGAME_SCRIPTS:
            continue
        for m in re.finditer(r'ingame_trade\s+(INGAME_TRADE_[A-Z0-9_]+)',
                             open(path, encoding='utf-8', errors='ignore').read()):
            if m.group(1) in deal:
                out.append((name,) + deal[m.group(1)])
    return out


def starters(sources):
    src = open('src/starter_choose.c', encoding='utf-8').read()
    for m in re.finditer(r'#define\s+\w+_STARTER\s+\(IS_FRLG\s*\?\s*SPECIES_[A-Z0-9_]+\s*:\s*(SPECIES_[A-Z0-9_]+)', src):
        sources[m.group(1)].add('starter')


def collect():
    """{SPECIES_X: {how you get it}} for everything obtainable pre-post-game."""
    sources = collections.defaultdict(set)
    wild(sources)
    scripts(sources)
    starters(sources)
    for sp in UNREACHABLE:
        sources.pop(sp, None)

    blocks = species_blocks()
    evos = {sp: re.findall(r'SPECIES_[A-Z0-9_]+', field(b, 'evolutions') or '')
            for sp, b in blocks.items()}
    # Evolutions forward, and breeding backwards: a Wobbuffet gives you Wynaut.
    pre = collections.defaultdict(list)
    for sp, targets in evos.items():
        for t in targets:
            pre[t].append(sp)
    def close(frontier):
        while frontier:
            sp = frontier.pop()
            for t in evos.get(sp, ()):
                if t not in sources:
                    sources[t].add('evolves from ' + sp.replace('SPECIES_', '').title())
                    frontier.append(t)
            for p in pre.get(sp, ()):
                if p not in sources:
                    sources[p].add('breed from ' + sp.replace('SPECIES_', '').title())
                    frontier.append(p)

    close(list(sources))
    # A trade only pays out if what it asks for is itself obtainable, and the
    # mon it hands over can unlock further trades, so run to a fixpoint.
    pending = offered_trades()
    while True:
        doable = [t for t in pending if t[2] in sources]
        if not doable:
            break
        pending = [t for t in pending if t not in doable]
        for where, give, want in doable:
            sources[give].add('trade: ' + where)
        close([g for _, g, _ in doable])
    global DEAD_TRADES
    DEAD_TRADES = pending
    return sources


def main():
    sources = collect()
    vals = species_values()
    blocks = species_blocks()
    nat = {sp: (re.search(r'\.natDexNum\s*=\s*NATIONAL_DEX_([A-Z0-9_]+)', b) or [None, ''])[1]
           for sp, b in blocks.items()}
    ordered = sorted(sources, key=lambda s: (vals.get(s) or 0))

    if '--json' in sys.argv:
        print(json.dumps({s: sorted(sources[s]) for s in ordered}, indent=1))
        return 0

    print(f'{len(ordered)} species obtainable before the post-game')
    print(f'{len(set(nat[s] for s in ordered if s in nat))} national dex slots\n')
    for s in ordered:
        print('%-32s %s' % (s.replace('SPECIES_', ''), '; '.join(sorted(sources[s]))))
    if DEAD_TRADES:
        print('\nTrades that can never happen (the mon they ask for is unobtainable):')
        for where, give, want in DEAD_TRADES:
            print('  %-28s gives %s for %s' % (where, give.replace('SPECIES_', ''),
                                               want.replace('SPECIES_', '')))
    print('\nDeliberately excluded:')
    for sp, why in UNREACHABLE.items():
        print('  %-20s %s' % (sp.replace('SPECIES_', ''), why))
    for k, why in list(POSTGAME_MAPS.items()) + list(POSTGAME_SCRIPTS.items()):
        print('  %-20s %s' % (k, why))
    return 0


if __name__ == '__main__':
    sys.exit(main())
