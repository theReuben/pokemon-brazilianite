from PIL import Image
import math
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/object_events/pics/people/team_aqua/archie.png'); px=im.load()
W,H=im.size; NF=W//16

# --- shades. His eyes are on row 19, at x 6 and 9 of each frame. --------
FACE={1,2,3,4,14,15}
for f in range(NF):
    x0=f*16
    for x in range(4,12):
        if px[x0+x,19] in FACE: px[x0+x,19]=13
    for x in (5,6,9,10):
        if px[x0+x,18] in FACE: px[x0+x,18]=13

# No dreadlocks here. Beside the head there are 14 free pixels across rows
# 15-24 and the rest is his shoulder, so a mass either reads as a speck or
# gets painted onto the jacket in the same near-black and disappears. At this
# size the dark head and shoulders already carry the silhouette.

PAL=[(115,197,164),
     (197,140, 98),(164,107, 74),(123, 74, 49),      # 1-3 skin
     ( 82, 49, 33),                                  # 4   skin shadow
     ( 74, 66, 82),( 90, 90, 98),( 33, 28, 38),      # 5 lit edge, 6 spare, 7 hair
     (148,107,222),(107, 74,180),( 66, 41,115),      # 8-10 the cap
     (238,197, 90),                                  # 11  gold
     ( 57, 57, 66),( 24, 24, 28),                    # 12-13 jacket shading, and the shades
     (255,222,131),                                  # 14  the cap's gold badge
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/liljon_ow.png')
im.convert('RGB').resize((W*8,H*8),Image.NEAREST).save(SP+'/liljon_ow_big.png')
print('built')
