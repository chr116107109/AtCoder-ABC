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


T1 = []

from collections import deque
def dfs(s):
    q = deque()
    q.append((s,0,-1))
    visited = {}
    while q:
        s,d,parent = q.pop()
        if s in visited:
            continue
        visited[s] = d
        if parent != -1:
            T1.append((parent,s))
        for t in g[s]:
            q.append((t,d+1,s))
    return visited

dfs(0)

T2 = []

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0,-1))
    visited = {}
    while q:
        s,d,parent = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        if parent != -1:
            T2.append((parent,s))
        for t in g[s]:
            q.append((t,d+1,s))
    return visited

bfs(0)

for s,t in T1:
    print(s+1,t+1)

for s,t in T2:
    print(s+1,t+1)