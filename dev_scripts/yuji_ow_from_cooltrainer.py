# -*- coding: utf-8 -*-
"""YUJI's overworld sprite, from the COOLTRAINER M the battle pic pairs with.

Same three groups as the battle sprite, and just as tidy:

    8,  9, 10   hair, which is most of the sprite in the back-facing frames
    11, 12, 13  the tracksuit, torso and legs together
    5,  6,  7   unused by this sprite, so the red collar costs nothing

The collar is the garment on rows 22-23, the two rows below the chin.
Everything below that is the uniform.
"""
import sys
from PIL import Image

BASE = 'graphics/object_events/pics/people/cooltrainer_m.png'
OUT_PNG = 'graphics/object_events/pics/people/yuji.png'
OUT_PAL = 'graphics/object_events/palettes/yuji.pal'

PAL = {
    0:  (115, 197, 164),
    1:  (255, 213, 180),        # skin, untouched
    2:  (246, 189, 148),
    3:  (222, 148, 115),
    4:  (123,  65,  65),
    5:  (255, 123, 115),        # collar, lit    (was unused)
    6:  (197,  49,  57),        # collar, mid    (was unused)
    7:  (140,  32,  40),        # collar, shadow (was unused)
    8:  (255, 180, 176),        # 157 -> 200  hair, highlight
    9:  (222, 106, 115),        # 101 -> 136  hair, mid
    10: (156,  57,  74),        #  64 ->  84  hair, shadow
    11: (108, 112, 126),        # 146 -> 110  uniform, lit
    12: ( 72,  74,  86),        #  96 ->  72  uniform, mid
    13: ( 44,  46,  56),        #  56 ->  46  uniform, shadow
    14: (255, 255, 255),
    15: (  0,   0,   0),
}
COLLAR = {11: 5, 12: 6, 13: 7}

im = Image.open(BASE)
W, H = im.size
assert (W, H) == (160, 32) and im.mode == 'P'
px = im.load()
for y in (22, 23):
    for x in range(W):
        if px[x, y] in COLLAR:
            px[x, y] = COLLAR[px[x, y]]

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
