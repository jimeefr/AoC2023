from common import read_input
from collections import defaultdict
import re,math

lines = read_input(8)

path = [ "LR".find(c) for c in lines[0] ]

G = {}
for l in lines[2:]:
    n,l,r = re.findall(r"(.*) = \((.*), (.*)\)",l)[0]
    G[n] = (l,r)
steps = 0
pos = 'AAA'
while pos != 'ZZZ':
    pos = G[pos][path[steps%len(path)]]
    steps += 1
print(steps)