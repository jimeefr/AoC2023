from common import read_input

lines = read_input(1)

def l2n(s):
    r=""
    for c in s:
        if c in "0123456789": r+=c
    if r: return int(r[0]+r[-1])
    return 0

s = 0
for l in lines: s+= l2n(l)
print(s)