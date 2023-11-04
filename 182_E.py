
from collections import defaultdict
H,W,N,M = map(int,input().split())

tate = [[] for i in range(H)]
yoko = [[] for i in range(W)]


ans = 0
state = {}
for i in range(N):
    a,b = map(int,input().split())
    tate[a-1].append(b-1)
    yoko[b-1].append(a-1)
    state[(a-1,b-1)] = 'L'

for i in range(M):
    a,b = map(int,input().split())
    tate[a-1].append(b-1)
    yoko[b-1].append(a-1)
    state[(a-1,b-1)] = 'B'

for i in range(H):
    tate[i].sort()
for i in range(W):
    yoko[i].sort()

import bisect
ans = 0
for i in range(H):
    for j in range(W):
        if (i,j) in state:
            if state[(i,j)] == 'L':
                ans += 1
            continue
        
        if tate[i]:
            indt = bisect.bisect_left(tate[i], j)
            if indt == 0:
                if state[(i,tate[i][0])] == 'L':
                    ans += 1
                    continue    
            if 0 < indt < len(tate[i]):
                if state[(i,tate[i][indt])] == 'L' or state[(i,tate[i][indt-1])] == 'L':
                    ans += 1
                    continue    
            if indt == len(tate[i]):
                if state[(i,tate[i][indt-1])] == 'L':
                    ans += 1
                    continue    
        if yoko[j]:
            indy = bisect.bisect_left(yoko[j], i)
            if indy == 0:
                if state[(yoko[j][0],j)] == 'L':
                    ans += 1
            if 0 < indy < len(yoko[j]):
                if state[(yoko[j][indy],j)] == 'L' or state[(yoko[j][indy-1],j)] == 'L':
                    ans += 1
            if indy == len(yoko[j]):
                if state[(yoko[j][indy-1],j)] == 'L':
                    ans += 1

print(ans)