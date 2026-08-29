# -*- coding: utf-8 -*-
"""YUJI's overworld sprite, from the COOLTRAINER M the battle pic pairs with.

Same three groups as the battle sprite, and just as tidy:

    8,  9, 10   hair, which is most of the sprite in the back-facing frames
    11, 12, 13  the tracksuit, torso and legs together

No red here. At 16x32 there is no row that reads as a collar: the top of
the torso IS the shoulder line, and the neck itself is hidden behind the
chin in every frame, so red on those rows comes out as shoulder pads.
The collar stays on the battle sprite, where there are pixels for it.
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
    5:  (255, 222,  74),        # unused by this sprite, as in the base
    6:  (213, 172,  32),
    7:  (131,  98,   0),
    8:  (255, 180, 176),        # 157 -> 200  hair, highlight
    9:  (222, 106, 115),        # 101 -> 136  hair, mid
    10: (156,  57,  74),        #  64 ->  84  hair, shadow
    11: (108, 112, 126),        # 146 -> 110  uniform, lit
    12: ( 72,  74,  86),        #  96 ->  72  uniform, mid
    13: ( 44,  46,  56),        #  56 ->  46  uniform, shadow
    14: (255, 255, 255),
    15: (  0,   0,   0),
}
im = Image.open(BASE)
W, H = im.size
assert (W, H) == (160, 32) and im.mode == 'P'
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
