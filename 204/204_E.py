

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b,c,d = map(int,input().split())
    g[a-1].append([b-1,c,d])
    g[b-1].append([a-1,c,d])

q = []
heappush(q,(0,0))
visited = {}
while q:
    dist,s= heappop(q)
    if s in visited:
        continue
    visited[s] = dist
    for [t,c,d] in g[s]:
        if dist > math.sqrt(d) - 1:
            heappush(q,(dist+c+d//(dist+1),t))
        else:
            x = max(math.floor(math.sqrt(d)) - 1, 0)
            y = math.floor(math.sqrt(d))

            T = min(c+d//(x+1)+x,c+d//(y+1)+y)
            heappush(q,(T,t))
    
if N-1 in visited:
    print(visited[N-1])
else:
    print(-1)