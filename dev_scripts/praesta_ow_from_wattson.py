# -*- coding: utf-8 -*-
"""PRAESTA's overworld sprite: WATTSON's, with the white hair browned.

WATTSON's overworld sprite draws his hair, beard and moustache as one
flat white (index 14), and uses it for nothing else, so the recolour is
a single palette entry. Not the battle sprite's (128,88,62), though:
his overworld coat is a mid brown of its own, and at that value the
beard sank into the coat. The hair goes darker than both, (74,54,40).

One catch worth recording: WATTSON's sprite runs on the SHARED npc_2
palette, so it cannot simply be recoloured in place - every NPC on that
slot would change with him. PRAESTA gets a copy of npc_2 with the one
colour altered, on PALSLOT_NPC_SPECIAL, like our other one-offs.
"""
import sys
from PIL import Image

BASE = 'graphics/object_events/pics/people/gym_leaders/wattson.png'
OUT_PNG = 'graphics/object_events/pics/people/praesta.png'
OUT_PAL = 'graphics/object_events/palettes/praesta.pal'
HAIR = (74, 54, 40)

im = Image.open(BASE)
W, H = im.size
assert (W, H) == (48, 32) and im.mode == 'P'
pal = im.getpalette()[:48]
colours = [tuple(pal[i * 3:i * 3 + 3]) for i in range(16)]
assert colours[14] == (255, 255, 255)
colours[14] = HAIR

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
    Image.open(OUT_PNG).convert('RGB').resize((W * 6, H * 6), Image.NEAREST).save(sys.argv[1])
print('wrote', OUT_PNG, OUT_PAL)
