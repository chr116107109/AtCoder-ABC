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
    a,b,x,y = map(int,input().split())
    g[a-1].append([b-1,x,y])
    g[b-1].append([a-1,-x,-y])


from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0,0))
    visited = {}
    while q:
        s,x,y = q.popleft()
        if s in visited:
            continue
        visited[s] = (x,y)
        for t,u,v in g[s]:
            q.append((t,x+u,y+v))
    return visited

visited = bfs(0)
for i in range(N):
    if i in visited:
        print(*visited[i])
    else:
        print('undecidable')