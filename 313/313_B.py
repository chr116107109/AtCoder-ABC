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
        for t in g[s][0]:
            q.append((t,d+1))
        for t in g[s][1]:
            q.append((t,d+1))
        
    return visited

q = []
for i in range(N):
    if len(g[i][1]) == 0:
        q.append(i)

if len(q) > 1:
    print(-1)
    sys.exit()

ans = q[0] + 1
A = []
while q:
    s = q.pop()
    A.append(s)
    for t in g[s][0]:
        g[t][1].remove(s)
        if len(g[t][1]) == 0:
            q.append(t)
            

if len(A) == N:
    print(ans)
else:
    print(-1)