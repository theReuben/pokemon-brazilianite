from PIL import Image
SP='/private/tmp/claude-501/-Users-reuben-IdeaProjects-global-rom-editor/801051d8-c7a8-49a7-bca9-d16fdea71c1b/scratchpad'
im=Image.open('graphics/trainers/front_pics/leader_roxanne.png'); px=im.load()

# Roxanne's bows and her tights share two slots. The bows stay bows, so up at
# head height they move to a pair of their own and the tights keep 12/13.
for y in range(0,27):
    for x in range(64):
        if px[x,y]==12: px[x,y]=10
        elif px[x,y]==13: px[x,y]=11
# Her shoes are drawn in the hair's slot. Frieren wears brown boots, so from
# the ankle down that slot becomes leather.
for y in range(55,64):
    for x in range(64):
        if px[x,y]==8: px[x,y]=5
        elif px[x,y]==12: px[x,y]=5
        elif px[x,y]==13: px[x,y]=9
# Roxanne's tie sits where Frieren's striped undershirt goes, so it keeps the
# dark slot and gains white bands on alternate rows.
CHEST={(x,y) for y in range(27,34) for x in range(26,34)}
for (x,y) in CHEST:
    if px[x,y] in (12,13) and y%2==0: px[x,y]=14

# gold trim: the capelet edge and the hem of the robe
for y in (28,38):
    run=[x for x in range(64) if px[x,y] in (6,7)]
    if run:
        best=[];cur=[run[0]]
        for a,b in zip(run,run[1:]):
            if b==a+1: cur.append(b)
            else:
                if len(cur)>len(best): best=cur
                cur=[b]
        if len(cur)>len(best): best=cur
        for x in best: px[x,y]=10
        px[best[0],y]=11; px[best[-1],y]=11

# Roxanne is built on dark hair against a light face. Frieren inverts that, so
# the hair takes the brightest value in the sprite and the skin drops well
# below it - 246 against 205 - or the two merge into one pale blur.
PAL=[(115,197,164),
     (238,197,180),(213,164,140),(172,123, 98),      # 1-3 skin      L 205/173/133
     (115, 90, 98),                                  # 4   shadow    L  96
     (156,115, 74),                                  # 5   boots
     (213,218,222),(148,156,164),                    # 6-7 robe      L 216/154
     (243,243,255),                                  # 8   hair      L 244, cooled
     ( 98, 74, 49),                                  # 9   boot dark
     (238,197, 90),(172,131, 49),                    # 10-11 gold, and her hair ties
     ( 90, 90,106),( 49, 49, 66),                    # 12-13 leggings L 91/51
     (255,255,255),
     (  0,  0,  0)]
flat=[]
for c in PAL: flat+=list(c)
im.putpalette(flat+[0]*(768-len(flat)))
im.save(SP+'/frieren.png')
im.convert('RGB').resize((64*7,64*7),Image.NEAREST).save(SP+'/frieren_big.png')
print('built')
