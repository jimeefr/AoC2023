from common import read_input

lines = read_input(10)
H,W=len(lines),len(lines[0])

S=None
for i,l in enumerate(lines):
    j=l.find('S')
    if j>=0:
        S=(i,j)
        break
else: assert False,'S not found'

Dirs={'S':[(0,1),(1,0),(0,-1),(-1,0)],'-':[(0,-1),(0,1)],'|':[(-1,0),(1,0)],
      'F':[(0,1),(1,0)],'7':[(1,0),(0,-1)],
      'L':[(-1,0),(0,1)],'J':[(-1,0),(0,-1)],
      '.':[]}

def neigh(i,j):
    n=[]
    for di,dj in Dirs[lines[i][j]]:
        ni,nj=i+di,j+dj
        if 0<=ni<H and 0<=nj<W: n.append((ni,nj))
    return n
def connected(i,j):
    n=[]
    for ni,nj in neigh(i,j):
        if (i,j) in neigh(ni,nj): n.append((ni,nj))
    return n
visited = set([S])
Q = [(S,0)]
further = S
while Q:
    (i,j),d = Q.pop(0)
    for ni,nj in connected(i,j):
        if (ni,nj) not in visited:
            further = d+1
            visited.add((ni,nj))
            Q.append(((ni,nj),d+1))
print(further)

#Fix S
si,sj=S
cs = connected(si,sj)
lines = [list(l) for l in lines]
trueS = None
if (si+1,sj) in cs:
    if (si,sj+1) in cs: trueS = 'F'
    elif (si-1,sj) in cs: trueS = '|'
    else: trueS = '7'
else:
    if (si,sj+1) in cs: 
        if (si,sj-1) in cs: trueS = '-'
        else: trueS = 'L'
    else: trueS = 'J'

inside = limit = False
count = 0
for i,l in enumerate(lines):
    assert not inside
    assert not limit
    for j,t in enumerate(l):
        if (i,j) in visited:
            if t=='S': t = trueS
            if t in 'F7LJ': limit = not limit
            if t in 'LJ|': inside = not inside
        else:
            assert not limit
            if inside: count+=1
print(count)