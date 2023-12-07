from common import read_input
from collections import defaultdict
import re,math

lines = read_input(7)

cards = "J23456789TQKA"
def score(hand):
    f,q,l,t,p = 0,0,0,0,0
    j = sum([1 for _ in hand if _== "J"])
    for c in cards[1:]:
        n = sum([1 for _ in hand if _== c])
        if n==5: f+=1
        if n==4: q+=1
        if n==3: t+=1
        if n==2: p+=1
    if j:
        if q: q,f=0,1
        elif t:
            if j==2: t,f=0,1
            else: t,q=0,1 
        elif p:
            if j==3: p,f=0,1
            elif j==2: p,q=0,1
            else:
                p-=1
                t=1
        else:
            if j==5: f+=1
            elif j==4: f+=1
            elif j==3: q+=1
            elif j==2: t+=1
            else: p+=1
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