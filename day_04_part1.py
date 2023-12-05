from common import read_input
from collections import defaultdict
import re

lines = read_input(4)

rep=+0
for card in lines:
    print(card)
    cardid,winning,numbers = re.findall(r"Card +([\d]+): (.*) \| (.*)",card)[0]
    winning = set(winning.split())
    numbers = set(numbers.split())
    score = len(winning.intersection(numbers))
    if score: rep += 1<<(score-1)
print(rep)