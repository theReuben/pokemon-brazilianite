#!/usr/bin/env python3
"""Report generated graphics whose committed .4bpp no longer matches its .png.

The .4bpp files are build artifacts that are not tracked in git, and the .d
files gcc writes list them as phony targets with no recipe. That combination
lets a build succeed against a stale - or even missing - .4bpp, so an edited
PNG can silently never reach the ROM. Run this after touching any sprite.

    python3 tools/check_stale_graphics.py [--fix]
"""
import filecmp, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULE = re.compile(r'^(\S+\.4bpp): %\.4bpp: %\.png\n\t\$\(GFX\) \$< \$@ ?(.*)$', re.M)
VARS = {'$(OBJEVENTGFXDIR)': 'graphics/object_events/pics'}


def rules():
    text = open(os.path.join(ROOT, 'spritesheet_rules.mk')).read()
    for name, value in VARS.items():
        text = text.replace(name, value)
    for m in RULE.finditer(text):
        yield m.group(1), m.group(2).split()


def main():
    fix = '--fix' in sys.argv
    gfx = os.path.join(ROOT, 'tools/gbagfx/gbagfx')
    stale, missing = [], []
    with tempfile.TemporaryDirectory() as tmp:
        for target, flags in rules():
            png = target[:-5] + '.png'
            if not os.path.exists(os.path.join(ROOT, png)):
                continue
            dest = os.path.join(ROOT, target)
            out = dest if fix else os.path.join(tmp, 'out.4bpp')
            if not os.path.exists(dest):
                missing.append(target)
                if not fix:
                    continue
            subprocess.run([gfx, os.path.join(ROOT, png), out] + flags,
                           check=False, capture_output=True)
            if not fix and os.path.exists(out) and not filecmp.cmp(dest, out, shallow=False):
                stale.append(target)

    if fix:
        print('Regenerated every sprite sheet from its PNG.')
        return 0
    for t in missing:
        print('MISSING %s' % t)
    for t in stale:
        print('STALE   %s' % t)
    if stale or missing:
        print('\n%d sheet(s) out of step with their PNG. Re-run with --fix, then '
              'delete build/emerald/src/event_object_movement.o and rebuild.'
              % (len(stale) + len(missing)))
        return 1
    print('All sprite sheets match their PNGs.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
