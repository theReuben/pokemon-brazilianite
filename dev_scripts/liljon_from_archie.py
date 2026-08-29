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

# The Team Aqua badge sits mid-chest where the pendant hangs. It is a 4x4
# diamond on plain jacket, so there is room to clear it and draw a dollar
# sign - three wide, five deep, with the stroke running a row past each end.
for y in range(27,35):
    for x in range(33,40): px[x,y]=8
DOLLAR = ["###",
          "##.",
          "###",
          ".##",
          "###"]
for dy,row in enumerate(DOLLAR):
    for dx,ch in enumerate(row):
        if ch=='#': px[35+dx, 29+dy]=9
px[36,28]=9                      # the stroke, above
px[36,34]=9                      # and below
for y in (29,31,33): px[35,y]=14 # a highlight down the left edge


# --- dreadlocks: one mass on his left, not separate ropes. Individual locks
#     at this size read as sticks; the eye wants a silhouette. ------------
import math
TOP, BOT = 8, 21
for y in range(TOP, BOT+1):
    t=(y-TOP)/float(BOT-TOP)
    w=max(1,int(round(1+3.2*math.sin(min(1.0,t*1.5)*math.pi))))
    for k in range(w):
        x=40+k
        if 0<=x<64 and px[x,y]==0: px[x,y]=10
for p_ in [(x,y) for y in range(TOP-1,BOT+3) for x in range(18,50)
           if px[x,y]==0 and any(px[x+dx,y+dy]==10 for dx in(-1,0,1) for dy in(-1,0,1)
                                 if 0<=x+dx<64 and 0<=y+dy<64)]:
    px[p_]=15
for y in range(TOP+2, BOT-1):
    if px[40,y]==10 and px[40,y-1]==10: px[40,y]=5

PAL=[(115,197,164),
     (197,140, 98),(164,107, 74),(123, 74, 49),      # 1-3 skin
     ( 82, 49, 33),                                  # 4   skin shadow
     ( 74, 66, 82),                                  # 5   lit edge of the hair
     ( 90, 90, 98),( 66, 66, 74),( 41, 41, 49),      # 6-8 the jacket, black
     (238,197, 90),                                  # 9   the chain and pendant, gold
     ( 33, 28, 38),                                  # 10  the hair, L30
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
