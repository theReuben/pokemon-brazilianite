# -*- coding: utf-8 -*-
"""HUSH's overworld sprite: FRLG BILL's, with the hair taken down a shade.

BILL draws his hair in two golds, 6 and 7, and nothing else uses them.
The rest of him - lavender shirt, navy trousers, skin - is untouched.
"""
import sys
from PIL import Image

BASE = 'graphics/object_events/pics/people/bill.png'
OUT_PNG = 'graphics/object_events/pics/people/hush.png'
OUT_PAL = 'graphics/object_events/palettes/hush.pal'
HAIR = {6: (182, 143, 26), 7: (104,  76,   4)}   # was (213,172,32) and (131,98,0)

im = Image.open(BASE)
W, H = im.size
assert (W, H) == (144, 32) and im.mode == 'P'
pal = im.getpalette()[:48]
colours = [tuple(pal[i * 3:i * 3 + 3]) for i in range(16)]
for i, c in HAIR.items():
    colours[i] = c

flat = []
for c in colours:
    flat += list(c)
im.putpalette(flat + [0, 0, 0] * (256 - 16))
im.save(OUT_PNG)

with open(OUT_PAL, 'w') as f:
    f.write('JASC-PAL\n0100\n16\n')
    for c in colours:
        f.write('%d %d %d\n' % c)

if len(sys.argv) > 1:
    Image.open(OUT_PNG).convert('RGB').resize((W * 5, H * 5), Image.NEAREST).save(sys.argv[1])
print('wrote', OUT_PNG, OUT_PAL)
