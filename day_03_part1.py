from common import read_input
from collections import defaultdict
import re

lines = read_input(3)

rep = 0
for i,l in enumerate(lines):
    for m in re.finditer(r"(\d+)",l):
        a,b=m.span()
        t="".join([ t[max(a-1,0):b+1] for t in lines[max(i-1,0):i+2] ])
        if re.search(r"([^0-9.])",t): rep += int(m.group())
print(rep)

