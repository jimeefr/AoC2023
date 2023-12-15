from common import read_input
from collections import defaultdict
import re,math

lines = read_input(14)

def calc(l):
    score = len(l)
    total = 0
    border = True
    for i,c in enumerate(l):
        if c=='O':
            total += score
            score -=1
        elif c=='#':
            score = len(l)-i-1
    return total 

lines = [ "".join([l[i] for l in lines]) for i in range(len(lines[0]))]
print(sum([calc(l) for l in lines]))