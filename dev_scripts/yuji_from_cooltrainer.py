# -*- coding: utf-8 -*-
"""YUJI from the RS Cooltrainer M, who needs no pixels moved.

The base splits into three groups that never overlap:

    9, 10, 11   his hair, rows 2-17 only
    6,  7,  8   the whole tracksuit
    12, 13      the zip and collar trim

So this is a palette swap and nothing else. The one rule followed
throughout: keep each group's internal luminance spacing, and keep the
darkest garment tone clear of the outline's black, or the shading
collapses into a silhouette (learned the hard way on JAKE).
"""
import sys
from PIL import Image

BASE = 'graphics/trainers/front_pics/cooltrainer_m.png'
OUT_PNG = 'graphics/trainers/front_pics/yuji.png'
OUT_PAL = 'graphics/trainers/palettes/yuji.pal'

# index: (r, g, b)              original L -> new L
PAL = {
    0:  (115, 197, 164),        # background, untouched
    1:  (255, 230, 205),        # skin, untouched
    2:  (246, 205, 156),
    3:  (205, 156, 115),
    4:  (115,  82,  65),
    5:  (124, 128, 142),        # 175 -> 128  uniform, highlight: this is
                                #              the lit edge of his arm and
                                #              leg, not skin
    6:  ( 96,  99, 112),        # 135 -> 100  uniform, lit
    7:  ( 66,  68,  80),        # 115 ->  69  uniform, mid
    8:  ( 40,  42,  52),        #  71 ->  42  uniform, shadow
    9:  (156,  57,  74),        #  74 ->  84  hair, shadow
    10: (255, 180, 176),        # 166 -> 200  hair, highlight
    11: (222, 106, 115),        # 108 -> 136  hair, mid
    12: (255, 123, 115),        # 242 -> 155  collar and trim, lit
    13: (197,  49,  57),        # 198 ->  95  collar and trim, shade
    14: (255, 255, 255),        # eye white
    15: (  0,   0,   0),        # outline
}

im = Image.open(BASE)
assert im.size == (64, 64) and im.mode == 'P'
px = im.load()

# The POKe BALL he tosses sits alone in rows 16-21, x36-41, with a clear
# row between it and his hand - and it is drawn in the tracksuit's own
# reds, so it would come out as a dark lump. YUJI throws punches.
for y in range(16, 22):
    for x in range(35, 43):
        px[x, y] = 0

# Two stray skin-tone pixels sit on his hip, where the base used them as
# a highlight on the tracksuit. They are the last orange on the outfit.
for y in range(36, 52):
    for x in range(64):
        if px[x, y] == 3:
            px[x, y] = 5

# The base's trim is one stripe from shoulder to ankle. YUJI's uniform is
# plain black, so the whole stripe joins the uniform...
for y in range(64):
    for x in range(64):
        if px[x, y] == 12:
            px[x, y] = 6
        elif px[x, y] == 13:
            px[x, y] = 7

# ...and the red goes where it belongs: the collar, the garment on the
# two rows under his jaw. Kept tight at two rows by choice - deeper rows
# run the red out along the shoulders, which reads heavier. Lit pixels
# take the bright red and shaded ones the dark, so the collar keeps the
# roundness already drawn.
UNIFORM_LIT, UNIFORM_DARK = (5, 6), (7, 8)
for y in (19, 20):
    for x in range(64):
        if px[x, y] in UNIFORM_LIT:
            px[x, y] = 12
        elif px[x, y] in UNIFORM_DARK:
            px[x, y] = 13

flat = []
for i in range(16):
    flat += list(PAL[i])
im.putpalette(flat + [0, 0, 0] * (256 - 16))
im.save(OUT_PNG)

with open(OUT_PAL, 'w') as f:
    f.write('JASC-PAL\n0100\n16\n')
    for i in range(16):
        f.write('%d %d %d\n' % PAL[i])

if len(sys.argv) > 1:                      # preview at 6x
    Image.open(OUT_PNG).convert('RGB').resize((384, 384), Image.NEAREST).save(sys.argv[1])
print('wrote', OUT_PNG, OUT_PAL)
