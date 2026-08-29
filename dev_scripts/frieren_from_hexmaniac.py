from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/trainers/front_pics/hex_maniac.png'); px=im.load()
def nb(x,y): return [px[x+dx,y+dy] for dx in(-1,0,1) for dy in(-1,0,1)
                     if (dx or dy) and 0<=x+dx<64 and 0<=y+dy<64]

# --- 1. her side hair is drawn partly in the outline's own black -----
HAIR={(x,y) for y in range(19,48) for x in list(range(18,27))+list(range(38,48))}
for (x,y) in HAIR:
    if px[x,y] in (12,13): px[x,y]=9
    elif px[x,y]==15 and not any(v==0 for v in nb(x,y)): px[x,y]=10

# --- 2. the witch hat comes off. The face starts at row 19, so the cut
#        is clean - but it leaves the top of her head undrawn. --------
for y in range(0,19):
    for x in range(64): px[x,y]=0
# draw a hair cap over the skull and blend it into the tails
import math
CX, TOP, BOT = 31.5, 12, 19
for y in range(TOP, BOT+1):
    t=(y-TOP)/float(BOT-TOP)
    half=3.5+6.0*math.sin(min(1.0,t*1.25)*math.pi/2)
    for x in range(64):
        if abs(x-CX) <= half:
            if px[x,y]==0: px[x,y]= 9 if abs(x-CX) < half-1.2 else 10
for y in range(TOP-1, BOT+2):        # outline the cap
    for x in range(64):
        if px[x,y] in (9,10) and any(v==0 for v in nb(x,y)):
            for dx in(-1,0,1):
                for dy in(-1,0,1):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<64 and 0<=ny<64 and px[nx,ny]==0 and ny<=BOT+1: px[nx,ny]=15

PAL=[(115,197,164),
     (238,197,180),(213,164,140),(172,123, 98),      # 1-3 skin
     (115, 90, 98),                                  # 4   shadow
     (222,226,230),(205,210,214),(180,186,192),      # 5-7 the robe, flattened
     ( 74, 74, 90),                                  # 8   robe deep shadow
     (243,243,255),(197,197,213),                    # 9-10 hair, and its shading
     (238,197, 90),(172,131, 49),                    # 11-12 gold trim
     ( 90, 74, 57),                                  # 13  boots
     (255,255,255),
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/frieren_hex.png')
im.convert('RGB').resize((64*7,64*7),Image.NEAREST).save(SP+'/frieren_hex_big.png')
print('built')
