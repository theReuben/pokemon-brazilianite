from PIL import Image
from collections import deque
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/trainers/front_pics/juggler_frlg.png'); px=im.load()

def flood(seeds, allowed):
    seen=set(seeds); q=deque(seeds); out=set()
    while q:
        x,y=q.popleft()
        if not(0<=x<64 and 0<=y<64) or px[x,y] not in allowed: continue
        out.add((x,y))
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            n=(x+d[0],y+d[1])
            if n not in seen: seen.add(n); q.append(n)
    return out
def nb(x,y): return [px[x+dx,y+dy] for dx in(-1,0,1) for dy in(-1,0,1)
                     if (dx or dy) and 0<=x+dx<64 and 0<=y+dy<64]

# --- 1. the cape and the sack go; the juggled balls stay -------------
for p in flood([(55,45)],{6,7}) | flood([(45,39)],{4,11}) | flood([(25,30)],{4,11}):
    px[p]=0
BODY={1,2,3,6,7,8,9,10,11,12,13,14}
for _ in range(40):                     # outline left with nothing to outline
    gone=[(x,y) for y in range(24,58) for x in range(44,64)
          if px[x,y] in (5,15) and 0 in nb(x,y) and not any(v in BODY for v in nb(x,y))]
    if not gone: break
    for p in gone: px[p]=0
for _ in range(4):
    gone=[(x,y) for y in range(64) for x in range(64)
          if px[x,y]!=0 and all(v==0 for v in nb(x,y))]
    if not gone: break
    for p in gone: px[p]=0

# Indices 4 and 11 were the juggler's brown and orange: cape, balls, and the
# shading on his face and hands. The cape is gone and the two slots are being
# repurposed as pink and gold, so the shading left on the figure has to move to
# a skin tone first, or it turns into stray pink blotches. The balls keep theirs.
for y in range(10,64):
    for x in range(0,46):
        if px[x,y] in (4,11): px[x,y]=3

# --- 2. reassign regions the palette alone cannot separate ----------
for y in range(0,17):                   # the beanie is the bulk of his hair
    for x in range(64):
        if px[x,y]==7: px[x,y]=9
        elif px[x,y]==6: px[x,y]=8
for y in range(24,34):                  # the shirt front is the top, not skin
    for x in range(29,36):
        if px[x,y] in (12,13,14): px[x,y]=5
for y in range(18,20):                  # the scarf over his shoulder is part of the top
    for x in range(36,44):
        if px[x,y] in (6,7): px[x,y]=5
for y in range(20,24):                  # collar and shoulder become the gold trim,
    for x in range(28,43):              # starting below the jaw so his mouth stays clear
        if px[x,y] in (6,7): px[x,y]=11
for y in range(15,20):                  # the juggler's orange mouth reads as lipstick
    for x in range(30,36):
        if px[x,y]==11: px[x,y]=4
# His eyes sit at (29,14) and (33,13) - the face is turned slightly, so the
# marks go under each one rather than at a matched height.
px[29,15]=11                            # gold star, on the cheek under his left eye
px[34,15]= 4                            # pink teardrop, under his right

# --- 3. Hisoka's own details ----------------------------------------
SKIN={12,13,14,1,2,3}
for y in (34,35,36):                    # the sash
    for x in range(64):
        if px[x,y]==5: px[x,y]=4
# No armbands. They were mine, not his, and at this size two pink rows
# across a bare forearm read as a stripe painted on the arm.

PAL=[(213,222,238),
     (255,228,214),(238,190,164),(222,156,140),
     (222, 66,123),
     ( 41, 33, 49),
     (197,205,214),(247,247,250),
     (148, 24, 66),(214, 41, 74),(255, 98,115),
     (255,205, 74),
     (205,148,132),(238,180,164),(255,214,200),
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save('graphics/trainers/front_pics/hisoka.png')
im.convert('RGB').resize((64*7,64*7),Image.NEAREST).save(SP+'/hisoka_big.png')
print('built')
