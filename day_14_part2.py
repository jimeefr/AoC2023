from common import read_input
from collections import defaultdict
import re,math

lines = read_input(14)

def west(grid):
    res = []
    for line in grid:
        l = list(line)
        for i,ci in enumerate(l):
            if ci == '.':
                for j,cj in enumerate(l[i+1:]):
                    if cj == '#': break
                    elif cj == 'O':
                        l[i],l[i+j+1]=l[i+j+1],l[i]
                        break
        res.append("".join(l))
    return res

def east(grid):
    grid = [ l[::-1] for l in grid ]
    grid = west(grid)
    grid = [ l[::-1] for l in grid ]
    return grid

def north(grid):
    grid = [ "".join([l[i] for l in grid]) for i in range(len(grid[0]))]
    grid = west(grid)
    grid = [ "".join([l[i] for l in grid]) for i in range(len(grid[0]))]
    return grid

def south(grid):
    grid = [ "".join([l[i] for l in grid]) for i in range(len(grid[0]))]
    grid = east(grid)
    grid = [ "".join([l[i] for l in grid]) for i in range(len(grid[0]))]
    return grid

def cycle(grid): return east(south(west(north(grid))))

def calc(grid):
    s=0
    for i,l in enumerate(grid):
        s += sum([len(grid)-i for c in l if c == 'O'])
    return s
grid = lines

grids = {}
i=0
while i < 1000000000:
    grids["".join(grid)]=i
    i += 1
    grid = cycle(grid)
    if "".join(grid) in grids: 
        for j in range((1000000000-i)%(i-grids["".join(grid)])): grid = cycle(grid)
        break
print(calc(grid))