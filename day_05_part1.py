from common import read_input
from collections import defaultdict
import re

lines = read_input(5)
lines.append("")

seeds = list(map(int,lines[0].split(': ')[1].split()))
for l in lines[2:]:
    #print(l)
    if l=="":
        for i in range(len(seeds)):
            for d,s,n in M:
                if s<=seeds[i]<s+n:
                    seeds[i] += d-s
                    break
        print(seeds)
    elif l[-1]== ":": M = []
    else:
        M.append(list(map(int,l.split())))
    
print(min(seeds))