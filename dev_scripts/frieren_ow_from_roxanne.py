from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/object_events/pics/people/gym_leaders/roxanne.png'); px=im.load()
W,H=im.size
def nb(x,y): return [px[x+dx,y+dy] for dx in(-1,0,1) for dy in(-1,0,1)
                     if (dx or dy) and 0<=x+dx<W and 0<=y+dy<H]
src=[[px[x,y] for x in range(W)] for y in range(H)]
for y in range(H):
    for x in range(W):
        v=src[y][x]
        if y<=26:
            if v in (5,6,7): px[x,y]=11               # bows and trim -> gold
        elif y<=28:
            if v in (8,9,10): px[x,y]={8:6,9:7,10:7}[v]
            elif v in (5,6): px[x,y]=6
        else:
            if v in (5,6,7,8,9,10): px[x,y]=5         # boots
# Her hair is drawn with the outline's black woven through it. That reads fine
# on black hair and as a checkerboard on white, so interior black up in the
# hair - black with no open space beside it - becomes a hair shade.
for y in range(10,24):
    for x in range(W):
        if px[x,y]==15 and not any(v==0 for v in nb(x,y)): px[x,y]=13
PAL=[(115,197,164),
     (255,222,205),(238,189,164),(197,148,123),      # 1-3 skin, lifted so the
     (115, 98,106),                                  # 4   the sprite's own shadow
     (148,107, 66),                                  # 5   boots
     ( 90, 90,106),( 49, 49, 66),                    # 6-7 leggings
     (222,226,230),(172,180,189),(131,140,148),      # 8-10 robe
     (238,197, 90),                                  # 11  gold trim and hair ties
     (246,246,255),(164,164,189),                    # 12-13 hair, shade dropped
                                                     #       so the face reads
     (255,255,255),
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/frieren_ow.png')
im.convert('RGB').resize((W*8,H*8),Image.NEAREST).save(SP+'/frieren_ow_big.png')
print('built')
