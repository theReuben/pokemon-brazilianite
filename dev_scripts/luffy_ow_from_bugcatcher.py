from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/object_events/pics/people/bug_catcher.png'); px=im.load()
W,H=im.size
# The blue is his hat band, but also the shading under the brim two rows
# above it, and his shirt lower down. Only row 17 is the band.
for y in range(H):
    for x in range(W):
        v=px[x,y]
        if v in (8,9,10):
            if y==17:      px[x,y]={8:5,9:6,10:7}[v]      # the band -> red
            elif y<17:     px[x,y]={8:11,9:12,10:13}[v]   # brim shading -> straw
            elif y<=22:    px[x,y]={8:11,9:12,10:13}[v]   # collar shading -> straw
            elif y<=27:    px[x,y]={8:5,9:6,10:7}[v]      # shirt -> the vest
for y in (28,29):                                          # shorts -> blue
    for x in range(W):
        if px[x,y] in (11,12,13): px[x,y]={11:8,12:9,13:10}[px[x,y]]
# his vest hangs open on the three front-facing frames
for f in (0,3,4):
    x0=f*16
    for y in (23,24,25,26):
        for x in (7,8):
            if px[x0+x,y] in (5,6,7): px[x0+x,y]=2
PAL=[(115,197,164),
     (255,213,180),(255,197,148),(222,148,115),      # 1-3 skin
     (123, 65, 65),                                  # 4   shadow
     (255, 98, 98),(214, 41, 49),(140, 24, 41),      # 5-7 the red vest and hat band
     (148,197,246),( 90,139,189),( 16, 49, 82),      # 8-10 blue shorts
     (238,214,140),(197,164, 90),(115, 90, 41),      # 11-13 straw hat, and his sandals
     (255,255,255),
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/luffy_ow.png')
im.convert('RGB').resize((W*6,H*6),Image.NEAREST).save(SP+'/luffy_ow_big.png')
n=sum(1 for y in range(H) for x in range(W) if px[x,y] in (8,9,10) and y<28)
print('blue pixels above the shorts:', n)
