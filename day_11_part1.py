from common import read_input
from collections import defaultdict
import re,math

lines = read_input(11)

galaxies = []
empty_lines = []
empty_rows = []

for l,s in enumerate(lines):
    for r,c in enumerate(s):
        if c == '#': galaxies.append((r,l))
    if not '#' in s: empty_lines.append(l)
for r in range(len(lines[0])):
    row = [l[r] for l in lines]
    if not '#' in row: empty_rows.append(r)

def dist(g1,g2,expansion):
    (gr1,gl1),(gr2,gl2)=g1,g2
    d = abs(gr2-gr1)+abs(gl2-gl1)
    for r in empty_rows:
        if min(gr1,gr2)<r<max(gr1,gr2): d+=expansion
    for l in empty_lines:
        if min(gl1,gl2)<l<max(gl1,gl2): d+=expansion
    return d

total = 0
for i,gi in enumerate(galaxies):
    for j,gj in enumerate(galaxies[i+1:]):
        total += dist(gi,gj,1)
print(total)