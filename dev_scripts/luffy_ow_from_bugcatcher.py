from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/object_events/pics/people/bug_catcher.png'); px=im.load()
W,H=im.size
# The bug catcher already wears a straw hat. What has to move is the colour of
# the hat band, the shirt and the shorts - and the frames are row-aligned.
for y in range(H):
    for x in range(W):
        v=px[x,y]
        if 16<=y<=17 and v in (9,10): px[x,y]={9:6,10:7}[v]      # hat band -> red
        elif 23<=y<=27 and v in (8,9,10): px[x,y]={8:5,9:6,10:7}[v]  # shirt -> the vest
        elif 28<=y<=29 and v in (11,12,13): px[x,y]={11:8,12:9,13:10}[v]  # shorts -> blue
PAL=[(115,197,164),
     (255,213,180),(255,197,148),(222,148,115),      # 1-3 skin
     (123, 65, 65),                                  # 4   shadow
     (255, 98, 98),(214, 41, 49),(140, 24, 41),      # 5-7 the red vest (slots the bug catcher never used)
     (148,197,246),( 90,139,189),( 16, 49, 82),      # 8-10 blue shorts
     (238,214,140),(197,164, 90),(115, 90, 41),      # 11-13 straw hat, and his sandals
     (255,255,255),
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/luffy_ow.png')
im.convert('RGB').resize((W*6,H*6),Image.NEAREST).save(SP+'/luffy_ow_big.png')
print('built')
