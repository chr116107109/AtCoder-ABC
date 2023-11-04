
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

g = [[set(),set()] for i in range(N)]
f = {}
for i in range(M):
    a,b,c,d = map(int,input().split())
    g[a-1][0].add(b-1)
    g[b-1][1].add(a-1)
    if (a-1,b-1) in f:
        f[(a-1,b-1)].add((c,d))
    else:
        f[(a-1,b-1)] = {(c,d)}

d = [[0,1] for i in range(N)] 
d[-1] = [0,0]
q = []
for i in range(N-1):
    if len(g[i][0]) == 0:
        q.append(i)
        
while q:
    s = q.pop()
    #print(s)
    for t in g[s][1]:
        g[t][0].remove(s)
        if len(g[t][0]) == 0:
            q.append(t)

q = [N-1]

while q:
    s = q.pop()
    #print(s)
    for t in g[s][1]:
        
        for score,cost in f[(t,s)]:
            if d[t][0]/d[t][1] <= (d[s][0]+score)/(d[s][1]+cost):
                d[t][0] = d[s][0]+score
                d[t][1] = d[s][1]+cost
        
        g[t][0].remove(s)
        if len(g[t][0]) == 0:
            q.append(t)


print(d[0][0]/d[0][1])
