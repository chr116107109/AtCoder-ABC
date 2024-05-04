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
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in g[s]:
            q.append((t,d+1))
    return visited

visted = {}
ans = 0
for i in range(N):
    
    if i in visted:
        continue
    v = bfs(i)
    relations = 0
    for k in v:
        visted[k] = v[k]
        relations += len(g[k])

    ans += math.comb(len(v),2) - relations//2

print(ans)