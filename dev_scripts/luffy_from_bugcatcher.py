from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/trainers/front_pics/bug_catcher.png'); px=im.load()
def nb(x,y): return [px[x+dx,y+dy] for dx in(-1,0,1) for dy in(-1,0,1)
                     if (dx or dy) and 0<=x+dx<64 and 0<=y+dy<64]
# --- the net and its handle -----------------------------------------
for y in range(8,32):
    for x in range(40,64): px[x,y]=0
for _ in range(8):
    gone=[(x,y) for y in range(8,34) for x in range(30,64)
          if px[x,y]==15 and not any(1<=v<=14 for v in nb(x,y))]
    if not gone: break
    for p in gone: px[p]=0
for _ in range(4):
    gone=[(x,y) for y in range(64) for x in range(64)
          if px[x,y]!=0 and all(v==0 for v in nb(x,y))]
    if not gone: break
    for p in gone: px[p]=0
# --- index 8 is the tank top's shadow above the waist and his shoes
#     below it, so it has to be split before the palette changes ------
for y in range(64):
    for x in range(64):
        if px[x,y]==8: px[x,y] = 13 if y<=41 else 9
# --- the shorts are drawn in the outline's own black ------------------
for y in range(38,48):
    for x in range(18,42):
        if px[x,y]==15 and not any(v==0 for v in nb(x,y)): px[x,y]=9
PAL=[(115,197,164),
     (255,222,205),(230,180,148),(213,148,115),      # 1-3 skin
     (123, 90, 82),                                  # 4   shadow
     (246,222,156),(205,180,106),(140,115, 57),      # 5-7 straw hat
     (255,255,255),                                  # 8   (freed)
     ( 57,106,189),( 33, 57,115),                    # 9-10 shorts and shoes
     (222, 49, 57),                                  # 11
     (238, 66, 66),(172, 24, 41),                    # 12-13 the red vest
     (255,255,255),
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/luffy_front.png')
im.convert('RGB').resize((64*7,64*7),Image.NEAREST).save(SP+'/luffy_front_big.png')
print('built')
