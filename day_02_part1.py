from common import read_input
from collections import defaultdict
import re

lines = read_input(2)

gidsum = 0
for l in lines:
    print(l)
    gid,sets = re.findall(r"Game ([\d]+): (.*)",l)[0]
    gid=int(gid)
    sets = sets.split('; ')
    possible = True
    for s in sets:
        colorsum = defaultdict(int)
        colors = s.split(', ')
        for c in colors:
            n,color = re.findall(r"([\d]+) (.*)",c)[0]
            n=int(n)
            colorsum[color]+=n
        print(colorsum)
        if colorsum["red"]>12 or colorsum["green"]>13 or colorsum["blue"]>14: possible = False
    if possible:
        print("ok")
        gidsum += gid

print(gidsum)