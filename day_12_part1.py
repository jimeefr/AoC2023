from common import read_input

lines = read_input(12)

from functools import lru_cache
@lru_cache(maxsize=1000000)
def possibilities(springs,runs,inside = False):
    if inside:
        if springs == "":
            if len(runs)==1 and runs[0] == 0: r = 1
            else: r = 0
        elif springs[0] == ".":
            if runs[0] == 0: r = possibilities(springs[1:],runs[1:])
            else: r = 0
        elif springs[0] == "#": r = possibilities(springs[1:],(runs[0]-1,)+runs[1:],True)
        else:
            r = possibilities(springs[1:],(runs[0]-1,)+runs[1:],True)
            if runs[0] == 0: r += possibilities(springs[1:],runs[1:])
    else:
        if springs == "":
            if runs: r = 0
            else: r = 1
        elif springs[0] == ".": r = possibilities(springs[1:],runs)
        elif springs[0] == "#":
            if runs: r = possibilities(springs[1:],(runs[0]-1,)+runs[1:],True)
            else: r = 0
        else:
            r = possibilities(springs[1:],runs)
            if runs: r += possibilities(springs[1:],(runs[0]-1,)+runs[1:],True)
    #print(springs,runs,inside,r)
    return r

s = 0
for l in lines:
    springs,runs = l.split(" ")
    runs = tuple(map(int,runs.split(",")))
    p = possibilities(springs,runs)
    print(springs,runs,p)
    s += p
print(s)