

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
    a,b,c = map(int,input().split())
    g[a-1].append([b-1,c])
    g[b-1].append([a-1,-c])


def bfs(s,visited):
    q = deque()
    q.append((s,0))
    ok = True
    while q:
        s,d = q.popleft()
        if s in visited:
            if visited[s] != d:
                ok = False
                break
            continue
        visited[s] = d
        for t,c in g[s]:
            q.append((t,d+c))
    return visited,ok

visited = {}
ans = True
for i in range(N):
    if not i in visited:
        visited,ok = bfs(i,visited)
        ans &= ok

if ans:
    print('Yes')
else:
    print('No')
