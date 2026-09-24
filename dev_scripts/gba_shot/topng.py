import sys, zlib, struct
def png(raw, out, w=240, h=160, order="bgr", scale=1):
    d=open(raw,'rb').read()
    px=[]
    for y in range(h):
        row=[]
        for x in range(w):
            b0,b1,b2,b3=d[(y*w+x)*4:(y*w+x)*4+4]
            row.append((b2,b1,b0) if order=="bgr" else (b0,b1,b2))
        px.append(row)
    rows=b''
    for y in range(h):
        for _ in range(scale):
            line=bytearray()
            for x in range(w):
                for _ in range(scale): line+=bytes(px[y][x])
            rows+=b'\x00'+bytes(line)
    def chunk(t,data):
        c=t+data
        return struct.pack('>I',len(data))+c+struct.pack('>I',zlib.crc32(c)&0xffffffff)
    o=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',w*scale,h*scale,8,2,0,0,0))
    o+=chunk(b'IDAT',zlib.compress(rows,9))+chunk(b'IEND',b'')
    open(out,'wb').write(o)
png(sys.argv[1], sys.argv[2], order=(sys.argv[3] if len(sys.argv)>3 else "bgr"), scale=int(sys.argv[4]) if len(sys.argv)>4 else 1)
