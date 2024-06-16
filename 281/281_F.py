

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

A.sort()

g = [{}]

for i in range(N):
    now = 0
    for j in range(29,-1,-1):
        b = pow(2,j)
        if A[i]//b in g[now]:
            now = g[now][A[i]//b]
            A[i] %= b
        else:
            g.append({})
            g[now][A[i]//b], now = len(g) - 1, len(g)-1
            A[i] %= b

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0,0))
    ans = 2**30
    visited = {}
    while q:
        s,d,score = q.popleft()
        if len(g[s]) == 0:
            ans = min(ans,score)
        if score > ans:
            continue
        bit = len(g[s]) - 1
        for t in g[s].values():
            q.append((t,d+1,score + bit*pow(2,29-d)))
    return visited,ans

_, ans = bfs(0)
print(ans)