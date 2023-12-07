from common import read_input
from collections import defaultdict
import re,math

lines = read_input(6)
b = int(lines[0].replace(' ','').split(':')[1])
c = int(lines[1].replace(' ','').split(':')[1])

d=b*b-4*c
if d>0:
    x1 = (b-math.sqrt(d))/2
    x2 = (b+math.sqrt(d))/2
    s1 = math.ceil(x1)
    s2 = math.floor(x2)
    if s1==x1: s1+=1
    if s2==x2: s2-=1
    s = max(0,1 + s2 - s1)
else: s = 0
print(s)
