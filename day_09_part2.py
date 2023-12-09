from common import read_input
from collections import defaultdict
import re,math

lines = read_input(9)

def extrapolate(l):
    if sum(l)==0: return 0
    ll = [ l[i+1]-l[i] for i in range(len(l)-1)]
    nn = extrapolate(ll)
    return l[0]-nn
s=0
for l in lines: s+= extrapolate(list(map(int,l.split())))
print(s)