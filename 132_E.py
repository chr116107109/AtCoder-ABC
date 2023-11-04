

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
g = [[set(),set()] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1][0].add(b-1)
    g[b-1][1].add(a-1)

s,t = map(int,input().split())
from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0,-1))
    visited = {}
    while q:
        s,d,count = q.popleft()
        if (s,count) in visited:
            continue
        visited[(s,count)] = d
        for t in g[s][0]:
            q.append((t,d+1,(count+1)%3))
    return visited

visited = bfs(s-1)
if (t-1,2) in visited:
    print(visited[(t-1,2)]//3)
else:
    print(-1)