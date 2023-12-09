from common import read_input
from collections import defaultdict
import re,math

lines = read_input(8)

path = [ "LR".find(c) for c in lines[0] ]

G = {}
for l in lines[2:]:
    n,l,r = re.findall(r"(.*) = \((.*), (.*)\)",l)[0]
    G[n] = (l,r)

starts = [n for n in G.keys() if n[-1]=="A"]

total = 1
for pos in starts:
    steps = 0
    while pos[-1] != "Z":
        pos = G[pos][path[steps%len(path)]]
        steps += 1
    assert steps%len(path)==0 # juste pour tester
    total = math.lcm(total,steps)
print(total)