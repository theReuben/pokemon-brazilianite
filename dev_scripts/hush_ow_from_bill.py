# -*- coding: utf-8 -*-
"""HUSH's overworld sprite: FRLG BILL's, matched to his battle pic.

BILL's overworld sprite draws his hair AND his trousers in the same two
golds, 6 and 7 - the trousers are khaki in the battle sprite too. Since
the trousers go black and the hair goes dark brown, the two have to be
split by row first: rows 26 down are legs and shoes, everything above
is hair. The legs move onto 11 and 12, which this sprite never uses.

The shirt (8, 9, 10) becomes the same deep navy as the battle pic.
"""
import sys
from PIL import Image

BASE = 'graphics/object_events/pics/people/bill.png'
OUT_PNG = 'graphics/object_events/pics/people/hush.png'
OUT_PAL = 'graphics/object_events/palettes/hush.pal'

PAL = {
    6:  ( 72,  54,  44),        # hair, lit    (was 213,172, 32)
    7:  ( 44,  32,  26),        # hair, shade  (was 131, 98,  0)
    8:  ( 74,  94, 164),        # shirt, lit   (was 164,139,238)
    9:  ( 38,  52, 116),        # shirt, mid   (was 106, 82,189)
    10: ( 20,  28,  72),        # shirt, shade (was  65, 57, 98)
    11: ( 56,  60,  68),        # trousers, lit   (was unused)
    12: ( 38,  42,  48),        # trousers, shade (was unused)
}
LEGS = {6: 11, 7: 12}

im = Image.open(BASE)
W, H = im.size
assert (W, H) == (144, 32) and im.mode == 'P'
px = im.load()
for y in range(26, H):
    for x in range(W):
        if px[x, y] in LEGS:
            px[x, y] = LEGS[px[x, y]]

pal = im.getpalette()[:48]
colours = [tuple(pal[i * 3:i * 3 + 3]) for i in range(16)]
for i, c in PAL.items():
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
