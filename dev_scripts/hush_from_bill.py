# -*- coding: utf-8 -*-
"""HUSH: the FRLG BILL trainer sprite, hair a shade darker.

The expansion ships 88 FRLG trainer pics but not BILL's - no FRLG
trainer ever battles as him - so the source here is the Gen III sprite
itself, kept beside this script as _bill_source.png. It arrives as
RGBA with exactly 15 colours plus transparency, which is already a
legal GBA palette; all this does is index it, put the standard trainer
background in slot 0, darken the three hair tones by about an
eighth, and repaint the shirt deep navy and the trousers black.

The darkest hair tone is also used on his shoes and a few outline
pixels, so those darken with it. At this size that reads as shadow
rather than a mistake, and keeping one index for both is what leaves
room for the rest of the palette.
"""
import sys
from PIL import Image

SRC = 'graphics/trainers/front_pics/_bill_source.png'
OUT_PNG = 'graphics/trainers/front_pics/hush.png'
OUT_PAL = 'graphics/trainers/palettes/hush.pal'
BG = (115, 197, 164)
RECOLOUR = {                  # was            -> now
    # hair, a shade darker
    (176, 136, 112): (154, 118,  96),
    (152, 104,  80): (132,  90,  68),
    (104,  72,  56): ( 90,  62,  48),
    # shirt, deep navy instead of BILL's purple
    (176, 136, 208): ( 74,  94, 164),
    (136,  96, 168): ( 38,  52, 116),
    ( 96,  64, 104): ( 20,  28,  72),
    # trousers, black instead of khaki. The darkest tone stops at L28
    # rather than true black, or the legs merge with the outline.
    (208, 184, 128): ( 76,  80,  90),
    (184, 160,  96): ( 56,  60,  68),
    (136, 120,  72): ( 38,  42,  48),
    ( 88,  72,  48): ( 26,  28,  34),
}

src = Image.open(SRC).convert('RGBA')
assert src.size == (64, 64)
px = src.load()

colours, seen = [BG], {BG: 0}
for y in range(64):
    for x in range(64):
        r, g, b, a = px[x, y]
        c = BG if a == 0 else RECOLOUR.get((r, g, b), (r, g, b))
        if c not in seen:
            seen[c] = len(colours)
            colours.append(c)
assert len(colours) <= 16, len(colours)

out = Image.new('P', (64, 64))
for y in range(64):
    for x in range(64):
        r, g, b, a = px[x, y]
        c = BG if a == 0 else RECOLOUR.get((r, g, b), (r, g, b))
        out.putpixel((x, y), seen[c])
flat = []
for c in colours + [(0, 0, 0)] * (16 - len(colours)):
    flat += list(c)
out.putpalette(flat + [0, 0, 0] * (256 - 16))
out.save(OUT_PNG)

with open(OUT_PAL, 'w') as f:
    f.write('JASC-PAL\n0100\n16\n')
    for c in colours + [(0, 0, 0)] * (16 - len(colours)):
        f.write('%d %d %d\n' % c)

if len(sys.argv) > 1:
    Image.open(OUT_PNG).convert('RGB').resize((448, 448), Image.NEAREST).save(sys.argv[1])
print('wrote', OUT_PNG, OUT_PAL, '(%d colours)' % len(colours))
