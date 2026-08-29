# -*- coding: utf-8 -*-
"""PRAESTA: WATTSON's sprite carrying BROCK's hair colour.

WATTSON's hair and beard are one white mass (9), its shadow (7) and a
few pure-white highlights (14). 9 and 7 live only on his head, rows
4-23, so they recolour wholesale. 14 is shared with a pixel on his coat,
so only the head's whites are moved - onto 9, since pure white reads as
a shine on white hair but as a bald patch on brown.

BROCK's exact browns, (197,148,115) and (123,90,82), do not survive the
move: his hair sits above pale skin with an outline between, while this
beard covers the face, and at those values it read as flesh. The browns
are darkened to (128,88,62) and (78,52,40) - the same hue, dropped
well clear of the skin ramp.
"""
import sys
from PIL import Image

BASE = 'graphics/trainers/front_pics/leader_wattson.png'
OUT_PNG = 'graphics/trainers/front_pics/praesta.png'
OUT_PAL = 'graphics/trainers/palettes/praesta.pal'

PAL = {
    0:  (115, 197, 164),
    1:  (255, 222, 205),        # skin, untouched
    2:  (238, 180, 148),
    3:  (197, 139, 106),
    4:  (123,  90,  82),
    5:  (164, 139,  90),        # coat and trousers, untouched
    6:  (131, 106,  74),
    7:  ( 78,  52,  40),        # 130 ->  57  hair, shadow
    8:  ( 82,  65,  74),
    9:  (128,  88,  62),        # 214 ->  96  hair, mass
    10: (255, 197,  90),
    11: (189, 156,  90),
    12: ( 57,  41,  49),
    13: (222, 115, 131),
    14: (255, 255, 255),
    15: (  0,   0,   0),
}

im = Image.open(BASE)
assert im.size == (64, 64) and im.mode == 'P'
px = im.load()
for y in range(0, 24):
    for x in range(64):
        if px[x, y] == 14:
            px[x, y] = 9

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
    Image.open(OUT_PNG).convert('RGB').resize((448, 448), Image.NEAREST).save(sys.argv[1])
print('wrote', OUT_PNG, OUT_PAL)
