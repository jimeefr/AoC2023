from common import read_input
from collections import defaultdict
import re,math

lines = read_input(13)
lines.append("")
grids = []
grid = []
for l in lines:
    if l: grid.append(l)
    else:
        grids.append(grid)
        grid = []

def refl(grid):
    n = len(grid)
    for x in range(1,n):
        is_ref = True
        for l in range(0,x):
            if 0<=2*x-l-1<n:
                is_ref = is_ref and (grid[l]==grid[2*x-l-1])
        if is_ref: return x

def swap(grid):
    return [ "".join([l[i] for l in grid]) for i in range(len(grid[0]))]

def ref(grid):
    r = refl(grid)
    if r: return 100*r
    gridd = swap(grid)
    r = refl(gridd)
    if not r: 
        print("\n".join(grid)+"\n")
        return 0
    return r

total = 0
for g in grids: total += ref(g)
print(total)
    

