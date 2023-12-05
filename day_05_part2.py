from common import read_input
from collections import defaultdict
import re

lines = read_input(5)
lines.append("")

seeds = list(map(int,lines[0].split(': ')[1].split()))
seeds = [tuple(seeds[2*i:2*i+2]) for i in range(len(seeds)//2)]
#print(seeds)
for l in lines[2:]:
    #print(l)
    if l=="":
        newseeds = []
        while seeds:
            sd,sl = seeds.pop()
            for d,s,n in M:
                if sd+sl <= s: continue
                elif s+n <= sd: continue
                else:
                    id = max(sd,s)
                    ie = min(sd+sl,s+n)
                    newseeds.append((id+d-s,ie-id))
                    if sd < id: seeds.append((sd,id-sd))
                    if sd+sl > ie: seeds.append((ie,sd+sl-ie))
                    break
            else: newseeds.append((sd,sl))
        seeds = newseeds
        #print(seeds)
    elif l[-1]== ":": M = []
    else:
        M.append(list(map(int,l.split())))
    
print(min(seeds)[0])