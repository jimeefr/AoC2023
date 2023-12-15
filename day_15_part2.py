from common import read_input
from collections import defaultdict
import re,math

lines = read_input(15)

def hash15(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h &= 255
    return h

hashmap = []
for i in range(256): hashmap.append(([],{}))
def store(s,f):
    p = hash15(s)
    if not s in hashmap[p][1]: hashmap[p][0].append(s)
    hashmap[p][1][s]=f
def remove(s):
    p = hash15(s)
    if s in hashmap[p][1]:
        hashmap[p][0].remove(s)
        del hashmap[p][1][s]

for instr in "".join(lines).split(','):
    if instr[-1] == '-': remove(instr[:-1])
    else:
        s,f = instr.split('=')
        store(s,f)

total = 0
for i,box in enumerate(hashmap):
    for j,lense in enumerate(box[0]):
        total += (i+1)*(j+1)*int(box[1][lense])

print(total)