from common import read_input
from collections import defaultdict
import re,math

lines = read_input(7)

cards = "23456789TJQKA"
def score(hand):
    f,q,l,t,p = 0,0,0,0,0
    for c in cards:
        n = sum([1 for _ in hand if _== c])
        if n==5: f+=1
        if n==4: q+=1
        if n==3: t+=1
        if n==2: p+=1
    if t and p:
        t=p=0
        l=1
    return (f,q,l,t,p,tuple((cards.find(c) for c in hand)))

hands = []
for l in lines:
    hand,bid = l.split()
    bid=int(bid)
    hands.append((hand,bid))
hands.sort(key = lambda h:score(h[0]))
scores = sum([h[1]*(i+1) for i,h in enumerate(hands)])
print(scores)