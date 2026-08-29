from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/object_events/pics/people/rocker.png'); px=im.load()
W,H=im.size
# The rocker's blond is used for his hair AND for parts of his kit, so the
# regions are split by row - the frames are all aligned to the same body.
for y in range(H):
    for x in range(W):
        v=px[x,y]
        if 25<=y<=26 and v==11: px[x,y]=9          # belt becomes the sash
        elif 22<=y<=26 and v in (5,6,7): px[x,y]=12 # chest emblem joins the top
        elif y>=27:
            if v in (5,6,7,11,12): px[x,y]=14       # legs become the white trousers
            elif v==13: px[x,y]=13
PAL=[(115,197,164),
     (255,228,214),(246,189,164),(222,156,132),      # 1-3 pale skin
     ( 74, 66, 82),                                  # 4   outline
     (255, 98,115),(214, 41, 74),(148, 24, 66),      # 5-7 hair
     (255,123,164),(222, 66,123),(156, 33, 82),      # 8-10 pink  (unused by the rocker)
     ( 66, 57, 82),( 41, 33, 49),                    # 11-12 the dark top
     (189,197,206),(247,247,250),                    # 13-14 white trousers
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/hisoka_ow.png')
im.convert('RGB').resize((W*6,H*6),Image.NEAREST).save(SP+'/hisoka_ow_big.png')
print('built', im.size)
