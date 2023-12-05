from common import read_input
from collections import defaultdict
import re

lines = read_input(4)
M = len(lines)

copies = [1]*M
rep=+0
for i,card in enumerate(lines):
    #print(card)
    cardid,winning,numbers = re.findall(r"Card +([\d]+): (.*) \| (.*)",card)[0]
    winning = set(winning.split())
    numbers = set(numbers.split())
    score = len(winning.intersection(numbers))
    #if score: score=1<<(score-1)
    rep += score*copies[i]
    for j in range(i+1,min(i+1+score,M)): copies[j]+=copies[i]
    #print(copies)
print(sum(copies))