# -*- coding: utf-8 -*-
"""DENJI's overworld sprite, from GIOVANNI's own.

The battle pic is the FRLG GIOVANNI, so his overworld sprite is the
honest base. It has the same shared-ramp problem and one piece of luck:

    12, 13   his hair AND his suit, so they split by row - the head is
             rows 11-21 in every frame, the body is 22 down
    7        hair only, the sides framing his face
    5, 6     unused, and already yellowish, so the blonde costs nothing
    8, 9, 10 GIOVANNI's orange shoes, rows 28-30 and nowhere else, which
             go black with the rest of the suit
"""
import sys
from PIL import Image

BASE = 'graphics/object_events/pics/people/giovanni.png'
OUT_PNG = 'graphics/object_events/pics/people/denji.png'
OUT_PAL = 'graphics/object_events/palettes/denji.pal'

PAL = {
    0:  (115, 197, 164),
    1:  (255, 213, 180),        # skin, untouched
    2:  (246, 189, 148),
    3:  (222, 148, 115),
    4:  (123,  65,  65),
    5:  (255, 227, 140),        # hair, light  (was unused)
    6:  (222, 176,  74),        # hair, mid    (was unused)
    7:  (176, 126,  45),        #  53 -> 133  hair, shadow: was hair already
    8:  ( 74,  78,  88),        # 139 ->  77  shoes, lit
    9:  ( 44,  46,  54),        #  82 ->  46  shoes, mid
    10: ( 24,  26,  32),        #  33 ->  26  shoes, shadow
    11: (197, 197, 213),        # shirt, untouched
    12: ( 92,  96, 104),        # 140 ->  96  suit, lit
    13: ( 56,  58,  68),        #  75 ->  58  suit, shadow
    14: (255, 255, 255),
    15: (  0,   0,   0),
}
HAIR = {12: 5, 13: 6}

im = Image.open(BASE)
W, H = im.size
assert (W, H) == (144, 32) and im.mode == 'P'
px = im.load()
for y in range(0, 22):
    for x in range(W):
        if px[x, y] in HAIR:
            px[x, y] = HAIR[px[x, y]]

flat = []
for i in range(16):
    flat += list(PAL[i])
im.putpalette(flat + [0, 0, 0] * (256 - 16))
im.save(OUT_PNG)

with open(OUT_PAL, 'w') as f:
    f.write('JASC-PAL\n0100\n16\n')
    for i in range(16):
        f.write('%d %d %d\n' % PAL[i])

if len(sys.argv) > 1:
    Image.open(OUT_PNG).convert('RGB').resize((W * 5, H * 5), Image.NEAREST).save(sys.argv[1])
print('wrote', OUT_PNG, OUT_PAL)
