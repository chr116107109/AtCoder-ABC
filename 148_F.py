import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,u,v = map(int,input().split())
g = [[] for i in range(N)]
for i in range(N-1):
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

aoki_visited = bfs(v-1)

q = deque()
q.append((u-1,0))
ans = 0
taka_visited = {}
while q:
    s,d = q.popleft()
    if s in taka_visited:
        continue
    ans = max(ans, aoki_visited[s])
    taka_visited[s] = d
    for t in g[s]:
        if aoki_visited[t] > d+1:
            q.append((t,d+1))

print(ans-1)