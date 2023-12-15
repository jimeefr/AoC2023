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

print(sum([hash15(s) for s in "".join(lines).split(',')]))