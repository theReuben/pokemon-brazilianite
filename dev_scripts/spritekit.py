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


# ---------------------------------------------------------------- checks


def components(s):
    """Every separate blob of drawn pixels, largest first.

    A finished trainer is one blob. Anything else is a leftover: the
    bandana knot that survived a colour sweep, a scrap of net beside the
    hand, straw specks above the brim. They are obvious once counted and
    almost invisible at 1:1.
    """
    seen, out = set(), []
    for sy in range(H):
        for sx in range(W):
            if s.px[sx, sy] == 0 or (sx, sy) in seen:
                continue
            blob, stack = set(), [(sx, sy)]
            while stack:
                x, y = stack.pop()
                if (x, y) in seen or not (0 <= x < W and 0 <= y < H) or s.px[x, y] == 0:
                    continue
                seen.add((x, y))
                blob.add((x, y))
                stack += [(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
            out.append(blob)
    return sorted(out, key=len, reverse=True)


def audit(s, name='sprite'):
    """Everything worth knowing before an import. Prints, returns clean."""
    blobs = components(s)
    gaps = holes(s)
    used, fits = check_palette(s)
    x0, y0, x1, y1 = bbox({(x, y) for x in range(W) for y in range(H) if s.px[x, y]})
    print(f'{name}: {x1 - x0 + 1}x{y1 - y0 + 1} at ({x0},{y0}), {len(used)} colours, fits={fits}')
    if len(blobs) > 1:
        print(f'  {len(blobs) - 1} detached piece(s): ' +
              ', '.join(f'{len(b)}px at {bbox(b)[:2]}' for b in blobs[1:][:5]))
    if gaps:
        print(f'  {len(gaps)} enclosed background pixel(s): {sorted(gaps)[:6]}')
    return not gaps and len(blobs) == 1 and fits


def plan_palette(s, need):
    """Which indices are free for new colour ramps, and what they cost.

    A 16-colour sprite has no spare room, so a transplant means taking
    indices from the base. Taking the wrong one is invisible until it is
    rendered: index 4 on the Aqua Admin looks like a rounding error at
    55 pixels, until those 55 turn out to be the shading on both
    shoulders. This ranks candidates by what they would cost and says
    where the losses are.
    """
    counts = {i: 0 for i in range(16)}
    where = {i: [] for i in range(16)}
    for y in range(H):
        for x in range(W):
            i = s.px[x, y]
            counts[i] += 1
            if len(where[i]) < 4:
                where[i].append((x, y))
    # 0 is the background and 15 the outline; neither is ever spare.
    spare = sorted((i for i in range(1, 15)), key=lambda i: counts[i])
    print(f'need {need} slot(s); cheapest to take:')
    for i in spare[:need + 3]:
        print(f'  index {i:2}  {counts[i]:5} px  e.g. {where[i]}')
    return spare[:need]


class Trace:
    """Snapshots each step so a bad one can be seen rather than deduced.

    Used as `t = Trace(sprite)` then `t.step('cut the bag')` after each
    edit; `t.save(path)` writes them as one strip, in order.
    """

    def __init__(self, sprite):
        self.sprite = sprite
        self.frames = [('start', sprite.im.copy())]

    def step(self, label):
        self.frames.append((label, self.sprite.im.copy()))

    def save(self, path, scale=3):
        from PIL import ImageDraw
        cw = W * scale + 10
        out = Image.new('RGB', (len(self.frames) * cw + 8, H * scale + 26), (24, 28, 36))
        d = ImageDraw.Draw(out)
        for i, (label, im) in enumerate(self.frames):
            out.paste(im.convert('RGB').resize((W * scale, H * scale), Image.NEAREST), (8 + i * cw, 8))
            d.text((8 + i * cw, H * scale + 12), label[:18], fill=(220, 225, 235))
        out.save(path)


def diff(before, after, path, scale=6):
    """Red for what went, green for what arrived, blue for recoloured.

    The erased thigh would have shown up here the moment it happened.
    """
    from PIL import ImageDraw
    out = Image.new('RGB', (W * scale, H * scale), (18, 20, 26))
    d = ImageDraw.Draw(out)
    for y in range(H):
        for x in range(W):
            a, b = before.px[x, y], after.px[x, y]
            if a == b:
                c = (60, 64, 74) if b else (18, 20, 26)
            elif b == 0:
                c = (220, 60, 60)
            elif a == 0:
                c = (60, 210, 110)
            else:
                c = (70, 140, 240)
            d.rectangle([x * scale, y * scale, x * scale + scale - 1, y * scale + scale - 1], fill=c)
    out.save(path)


def hole_regions(s):
    """Enclosed background, grouped into connected regions."""
    gaps = holes(s)
    out, seen = [], set()
    for start in gaps:
        if start in seen:
            continue
        blob, stack = set(), [start]
        while stack:
            p = stack.pop()
            if p in seen or p not in gaps:
                continue
            seen.add(p)
            blob.add(p)
            x, y = p
            stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        out.append(blob)
    return sorted(out, key=len, reverse=True)


def fill_holes(s, biggest=2):
    """Close background sealed inside the figure - but only the small ones.

    On the GBA an enclosed background pixel is not empty, it is the
    background colour showing through the middle of a trainer. Single
    pixels like that are always mistakes.

    Large ones are not. The gap between an arm and the body, the space
    between the legs, the inside of a raised elbow: all are enclosed
    background, and all are there on purpose. Filling one fuses the limb
    to the torso and the figure loses its depth - which is exactly what
    happened to Hisoka's right arm before this limit existed.

    Regions bigger than `biggest` are left alone and returned, so the
    caller can see what was deliberately skipped.
    """
    filled, kept = 0, []
    for region in hole_regions(s):
        if len(region) > biggest:
            kept.append(region)
            continue
        for x, y in region:
            near = [
                s.px[x + dx, y + dy]
                for dx in (-1, 0, 1)
                for dy in (-1, 0, 1)
                if (dx or dy) and 0 <= x + dx < W and 0 <= y + dy < H and s.px[x + dx, y + dy] != 0
            ]
            if near:
                s.px[x, y] = max(set(near), key=near.count)
                filled += 1
    return filled, kept


def outline_gaps(s):
    """Edge pixels that are not the outline colour.

    Gen 3 trainer sprites are drawn with a black line all the way round.
    Edits break it in two ways: recolouring a region can overwrite the
    line, and cutting a part away can expose an interior colour to the
    background. Both look like a soft or bleeding edge in the battle
    screen.

    Compare the count against the donor's rather than expecting zero -
    the official sprites leave a few edges open on purpose, usually
    where two limbs meet.
    """
    out = set()
    for y in range(H):
        for x in range(W):
            v = s.px[x, y]
            if v in (0, 15):
                continue
            if any(
                0 <= x + dx < W and 0 <= y + dy < H and s.px[x + dx, y + dy] == 0
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
            ):
                out.add((x, y))
    return out


def close_outline(s, gaps=None):
    """Put the missing line back, outside the figure where there is room.

    Writing the outline onto the exposed pixel itself would eat the
    figure a pixel at a time; the line belongs in the background next to
    it. Where the frame edge leaves no room, the pixel itself is used.
    """
    added = 0
    for x, y in sorted(gaps if gaps is not None else outline_gaps(s)):
        placed = False
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and s.px[nx, ny] == 0:
                s.px[nx, ny] = 15
                added += 1
                placed = True
        if not placed:
            s.px[x, y] = 15
            added += 1
    return added
