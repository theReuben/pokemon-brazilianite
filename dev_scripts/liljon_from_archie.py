from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/trainers/front_pics/aqua_leader_archie.png'); px=im.load()

# His eyes are at x 29-30 and x 34-35 on row 9. Two tall lenses rather than one
# band across the face - a solid bar reads as a visor - joined by a bridge only
# one row deep, and a temple arm out to each side.
FACE={1,2,3,4,14,15}
def put(x,y):
    if 0<=x<64 and 0<=y<64 and px[x,y] in FACE: px[x,y]=11
for y in (9,10,11):
    for x in range(28,32): put(x,y)      # left lens,  4 wide, 3 deep
    for x in range(34,38): put(x,y)      # right lens
for x in (32,33): put(x,9)               # the bridge, one row
for x in (27,38): put(x,9); put(x,10)    # temples

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
