import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools


N = int(input())

g = [set() for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].add(b-1)
    g[b-1].add(a-1)


q = deque()
for i in range(N):
    if len(g[i]) == 1:
        q.append(i)

visited = set()
ans = []
while q:
    #print(q)
    #print(g)
    s = q.popleft()
    
    if len(g[s]) != 1:
        continue

    center = list(g[s])[0]

    ans.append(len(g[center]))
    visited.add(center)
    for t in g[center]:
        g[t].remove(center)
        if len(g[t]) == 1:
            u = list(g[t])[0]
            q.append(u)
            g[t] = set()
            g[u].remove(t)
        visited.add(t)
    g[center] = set()
ans.sort()
print(*ans)

