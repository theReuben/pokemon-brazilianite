from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/trainers/front_pics/aqua_leader_archie.png'); px=im.load()

# Archie's eyes are on row 9. His shades are big rectangular wraparounds, so
# they take two full rows across the face and reach out past it at the temples.
FACE={1,2,3,4,14,15}
for y in (9,10):
    for x in range(28,41):
        if px[x,y] in FACE: px[x,y]=11
for y in (9,10):                      # temples, out to the edge of the head
    for x in (26,27,41,42):
        if px[x,y] in FACE: px[x,y]=11
for x in (29,30,38,39):               # a little depth under each lens
    if px[x,11] in FACE: px[x,11]=11

PAL=[(115,197,164),
     (197,140, 98),(164,107, 74),(123, 74, 49),      # 1-3 skin
     ( 82, 49, 33),                                  # 4   skin shadow
     (205,164, 90),                                  # 5   (spare)
     ( 90, 90, 98),( 66, 66, 74),( 41, 41, 49),      # 6-8 the jacket, black
     (238,197, 90),                                  # 9   the chain and pendant, gold
     (140, 98, 49),                                  # 10  (spare)
     ( 24, 24, 28),                                  # 11  the shades
     (123, 74,197),( 74, 41,123),                    # 12-13 the cap
     (255,222,131),                                  # 14  gold highlight
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/liljon.png')
im.convert('RGB').resize((64*7,64*7),Image.NEAREST).save(SP+'/liljon_big.png')
im.convert('RGB').crop((22,2,46,26)).resize((24*15,24*15),Image.NEAREST).save(SP+'/liljon_head.png')
print('built')
