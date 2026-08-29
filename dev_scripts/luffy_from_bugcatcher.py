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

# --- sandals. His trainers are drawn in 8, 9, 12, 13 and 14, the same
#     slots as the top and shorts, so they move to a slot of their own
#     before anything else is reassigned. -----------------------------
SHOE=({(x,y) for y in range(55,61) for x in range(18,27)} |
      {(x,y) for y in range(50,59) for x in range(37,48)})
for (x,y) in SHOE:
    if px[x,y] in (8,9,12,13,14): px[x,y]=11

# --- index 8 is the top's shadow above the waist, his legs below it ---
for y in range(64):
    for x in range(64):
        if px[x,y]==8: px[x,y] = 13 if y<=41 else 9
# --- the shorts share the outline's black; below the top only --------
for y in range(42,49):
    for x in range(18,42):
        if px[x,y]==15 and not any(v==0 for v in nb(x,y)): px[x,y]=9

PAL=[(115,197,164),
     (255,222,205),(230,180,148),(213,148,115),      # 1-3 skin
     (123, 90, 82),                                  # 4   shadow
     (246,222,156),(205,180,106),(140,115, 57),      # 5-7 straw hat
     (255,255,255),                                  # 8   unused
     ( 57,106,189),(246,238,213),                    # 9 shorts, 10 the hat's highlight
     (172,131, 74),                                  # 11  sandals
     (238, 66, 66),(172, 24, 41),                    # 12-13 the red vest
     (255,255,255),
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/luffy_front.png')
im.convert('RGB').resize((64*7,64*7),Image.NEAREST).save(SP+'/luffy_front_big.png')
print('built')
