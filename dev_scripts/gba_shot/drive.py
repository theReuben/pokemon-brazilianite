import subprocess, sys, os
S="/private/tmp/claude-501/-Users-reuben-IdeaProjects-pokemon-brazilianite/9abea950-5eaa-4c2c-8450-ca80bafe4694/scratchpad/run"
KEY=dict(A=0x1,B=0x2,SEL=0x4,START=0x8,RIGHT=0x10,LEFT=0x20,UP=0x40,DOWN=0x80)
def build(presses, shots, hold=6):
    args=[]
    for frame,name in presses:
        for f in range(frame, frame+hold):
            args.append(f"{f}:{KEY[name]:x}")
    args += [f"S:{f}" for f in shots]
    return args
def run(presses, shots, tag="", hold=6):
    for f in os.listdir(S):
        if f.startswith("frame_"): os.remove(os.path.join(S,f))
    args=build(presses,shots,hold)
    subprocess.run([f"{S}/driver", f"{S}/pokeemerald.gba", f"{S}/pokeemerald.sav", S]+args,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    out=[]
    for f in sorted(os.listdir(S)):
        if f.endswith(".raw"):
            png=os.path.join(S, tag+f.replace(".raw",".png"))
            subprocess.run(["python3", f"{S}/topng.py", os.path.join(S,f), png], check=True)
            out.append(png)
    print("\n".join(out))
if __name__=="__main__":
    exec(open(sys.argv[1]).read())
