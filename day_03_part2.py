from common import read_input
from collections import defaultdict
import re

lines = read_input(3)
M = len(lines)

rep = 0
gears = defaultdict(list)
for i,l in enumerate(lines):
    for m in re.finditer(r"(\d+)",l):
        a,b=m.span()
        partid = int(m.group())
        for j in range(max(0,i-1),min(M,i+2)):
            deb = max(a-1,0)
            g = re.search(r"(\*)",lines[j][deb:b+1])
            if g:
                gearid = j*10000+deb+g.span()[0]
                gears[gearid].append(partid)
for g in gears.values():
    if len(g) == 2: rep += g[0]*g[1]
print(rep)

