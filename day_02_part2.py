from common import read_input
from collections import defaultdict
import re

lines = read_input(2)

gidsum = 0
for l in lines:
    gid,sets = re.findall(r"Game ([\d]+): (.*)",l)[0]
    gid=int(gid)
    sets = sets.split('; ')
    colormax = defaultdict(int)
    for s in sets:
        colors = s.split(', ')
        for c in colors:
            n,color = re.findall(r"([\d]+) (.*)",c)[0]
            n=int(n)
            colormax[color]=max(colormax[color],n)
    power = 1
    for v in colormax.values(): power *= v
    gidsum += power

print(gidsum)