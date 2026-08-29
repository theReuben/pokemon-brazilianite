# -*- coding: utf-8 -*-
"""DENJI from the FRLG GIOVANNI, who already wears the suit.

GIOVANNI is the right silhouette for a Public Safety devil hunter: dark
suit, pale shirt, adult stance. Three things stand in the way.

  * his hair and his suit are drawn in the SAME two indices, 11 and 12,
    so blonde hair would mean a blonde suit. The hair lives in rows 0-8
    and nothing else up there is suit, so it is separated by row first.
  * only index 10 is free, and hair needs two tones. The POKe BALL he
    tosses and the ROCKET emblem on his pocket hold 5, 6 and 7 between
    them; DENJI has no use for either, so both come off and the indices
    are his hair's.
  * the emblem sits in a pocket drawn in the shirt's highlights, so the
    whole patch goes back to plain suit, not just the pink pixels.
  * the shaded side of his hair is drawn in the OUTLINE's own black, so
    recolouring 11 and 12 alone leaves a blonde cap on a black mass.
    Black inside the hair - black with no background beside it - becomes
    the hair's own shadow. Rows 0-8 only: his eyes are on row 9, and
    they are interior black too.
"""
import sys
from PIL import Image

BASE = 'graphics/trainers/front_pics/leader_giovanni_frlg.png'
OUT_PNG = 'graphics/trainers/front_pics/denji.png'
OUT_PAL = 'graphics/trainers/palettes/denji.pal'

PAL = {
    0:  (115, 197, 164),
    1:  (246, 222, 205),        # skin, untouched
    2:  (205, 180, 148),
    3:  (172, 131,  98),
    4:  (123,  90,  82),
    5:  (222, 176,  74),        # hair, mid    (was the ball's pink)
    6:  (216,  64,  56),        # the POKe BALL's red (was the emblem's)
    7:  (176, 126,  45),        # hair, shadow (was the ball's yellow)
    8:  (213, 213, 222),        # shirt, untouched
    9:  ( 41,  45,  49),        #  54 ->  44  suit, shadow
    10: (255, 227, 140),        # hair, light  (was unused)
    11: ( 86,  95, 104),        # 110 ->  93  suit, lit
    12: ( 58,  64,  68),        #  79 ->  63  suit, mid
    13: (148, 164, 172),        # shirt, shade
    14: (255, 255, 255),
    15: (  0,   0,   0),
}

im = Image.open(BASE)
assert im.size == (64, 64) and im.mode == 'P'
px = im.load()

# The POKe BALL he tosses, in rows 12-18. Its red and its sparkle were
# drawn in 5 and 7, which his hair now owns, so those pixels move onto
# index 6 - the one the ROCKET emblem freed - which is the ball's red.
# The sparkle keeps 7 and comes out gold, which suits it.
BALL = {5: 6, 4: 6}
for y in range(12, 19):
    for x in range(14, 22):
        if px[x, y] in BALL:
            px[x, y] = BALL[px[x, y]]

# The ROCKET pocket emblem. Everything in the patch becomes suit, so no
# pale outline is left ghosting where the pocket was.
for y in range(22, 27):
    for x in range(35, 41):
        if px[x, y] in (6, 11, 13, 8):
            px[x, y] = 12

# His hair, which shares 11 and 12 with the suit and is separated by row.
HAIR = {11: 10, 12: 5}
for y in range(0, 9):
    for x in range(64):
        if px[x, y] in HAIR:
            px[x, y] = HAIR[px[x, y]]

for y in range(0, 9):
    for x in range(64):
        if px[x, y] != 15:
            continue
        touches_bg = any(
            px[x + dx, y + dy] == 0
            for dx in (-1, 0, 1) for dy in (-1, 0, 1)
            if (dx or dy) and 0 <= x + dx < 64 and 0 <= y + dy < 64
        )
        if not touches_bg:
            px[x, y] = 7

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
    Image.open(OUT_PNG).convert('RGB').resize((512, 512), Image.NEAREST).save(sys.argv[1])
print('wrote', OUT_PNG, OUT_PAL)
