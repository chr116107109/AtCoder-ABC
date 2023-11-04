

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

q = deque() # (bit, last_visited, path_length)
inf = -1
visited = [[inf]*N for i in range(2**N)]
for i in range(N):
    q.append([1<<i, i])
    visited[1<<i][i] = 1
visited[0] = [0] * N 
while q:
    bit,parent = q.popleft()
    for t in g[parent]:
        next_bit = bit^(1<<t)
        if visited[next_bit][t] == inf:
            visited[next_bit][t] = visited[bit][parent] + 1
            q.append([next_bit, t])

ans = 0
for v in visited:
    ans += min(v)
print(ans)