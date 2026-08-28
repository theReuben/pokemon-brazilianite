"""Helpers for building trainer sprites out of existing ones.

Editing these by hand means naming coordinates and hoping. Every mistake
made so far came from that: clearing a *rectangle* to delete a satchel
took the leg behind it as well, and clearing another took a bite out of
a shoulder and left a hole ringed by its own outline.

So the unit of work here is a region, not a box:

    part = flood(sprite, 22, 20)       # the thing that pixel belongs to
    cut(sprite, part)                  # remove exactly that

and transplants are aligned by where a part sits rather than by an
offset guessed from a printout:

    hat = flood(catcher, 25, 21, colours=STRAW)
    paste(body, catcher, hat, align=('bottom', brow_row))

Everything works on palette indices, never RGB, because that is what a
GBA sprite is: 15 colours and a transparent one.
"""
from PIL import Image

W = H = 64


class Sprite:
    def __init__(self, path):
        im = Image.open(path)
        if im.mode != 'P':
            raise ValueError(f'{path} is not an indexed image')
        self.im = im
        self.px = im.load()
        self.pal = [tuple(im.getpalette()[i * 3:i * 3 + 3]) for i in range(16)]

    def save(self, path, palette=None):
        if palette:
            self.im.putpalette([c for rgb in palette for c in rgb])
        self.im.save(path)

    def copy(self):
        out = object.__new__(Sprite)
        out.im = self.im.copy()
        out.px = out.im.load()
        out.pal = list(self.pal)
        return out


def flood(s, x, y, colours=None):
    """The connected run of pixels reachable from (x, y).

    Without `colours` it spreads through the colour under the cursor;
    with them, through any of that set - which is how a whole hat, drawn
    in three straw tones plus its outline, comes out in one go.
    """
    want = set(colours) if colours else {s.px[x, y]}
    seen, stack = set(), [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in seen or not (0 <= cx < W and 0 <= cy < H):
            continue
        if s.px[cx, cy] not in want:
            continue
        seen.add((cx, cy))
        stack += [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]
    return seen


def outline_of(s, part):
    """The black pixels hugging a part, so it can be lifted with its line."""
    return {
        (x + dx, y + dy)
        for x, y in part
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if 0 <= x + dx < W and 0 <= y + dy < H and s.px[x + dx, y + dy] == 15
    }


def bbox(part):
    xs = [x for x, _ in part]
    ys = [y for _, y in part]
    return min(xs), min(ys), max(xs), max(ys)


def cut(s, part):
    for x, y in part:
        s.px[x, y] = 0


def paste(dst, src, part, dx=0, dy=0, remap=None):
    """Copy a part across, shifted, with its colours remapped."""
    remap = remap or {}
    for x, y in part:
        nx, ny = x + dx, y + dy
        if 0 <= nx < W and 0 <= ny < H:
            dst.px[nx, ny] = remap.get(src.px[x, y], src.px[x, y])


def recolour(s, part, remap):
    for x, y in part:
        if s.px[x, y] in remap:
            s.px[x, y] = remap[s.px[x, y]]


def orphans(s, passes=3, keep=2):
    """Outline left hanging once the thing it outlined has gone."""
    for _ in range(passes):
        for y in range(H):
            for x in range(W):
                if s.px[x, y] == 0:
                    continue
                near = sum(
                    1
                    for ax in (-1, 0, 1)
                    for ay in (-1, 0, 1)
                    if (ax or ay) and 0 <= x + ax < W and 0 <= y + ay < H
                    and s.px[x + ax, y + ay] != 0
                )
                if near < keep:
                    s.px[x, y] = 0


def holes(s):
    """Enclosed background - the tell-tale of a badly cut part.

    Background that cannot reach the edge of the frame is a hole inside
    the figure, which is what a rectangular cut leaves behind.
    """
    seen, stack = set(), [(x, y) for x in range(W) for y in (0, H - 1)]
    stack += [(x, y) for y in range(H) for x in (0, W - 1)]
    while stack:
        x, y = stack.pop()
        if (x, y) in seen or not (0 <= x < W and 0 <= y < H) or s.px[x, y] != 0:
            continue
        seen.add((x, y))
        stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    return {(x, y) for x in range(W) for y in range(H) if s.px[x, y] == 0 and (x, y) not in seen}


def grid(s, x0=0, y0=0, x1=W - 1, y1=H - 1):
    ch = '.123456789ABCDE#'
    out = ['     ' + ''.join(str(x % 10) for x in range(x0, x1 + 1))]
    for y in range(y0, y1 + 1):
        out.append(f'{y:3}  ' + ''.join(ch[s.px[x, y]] for x in range(x0, x1 + 1)))
    return '\n'.join(out)


def render(s, path, scale=10):
    s.im.convert('RGB').resize((W * scale, H * scale), Image.NEAREST).save(path)


def sheet(items, path, scale=5):
    """A labelled row of sprites, for comparing candidates."""
    from PIL import ImageDraw
    cw = W * scale + 14
    out = Image.new('RGB', (len(items) * cw + 8, H * scale + 26), (24, 28, 36))
    d = ImageDraw.Draw(out)
    for i, (name, spr) in enumerate(items):
        im = spr.im if isinstance(spr, Sprite) else Image.open(spr)
        out.paste(im.convert('RGB').resize((W * scale, H * scale), Image.NEAREST), (8 + i * cw, 8))
        d.text((8 + i * cw, H * scale + 12), name, fill=(220, 225, 235))
    out.save(path)


def check_palette(s):
    """What a sprite actually uses, and whether it still fits the GBA."""
    used = {s.px[x, y] for x in range(W) for y in range(H)}
    return sorted(used), len(used) <= 16
