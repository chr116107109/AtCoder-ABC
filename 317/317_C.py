import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())

g = [{} for i in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    g[a-1][b-1] = c
    g[b-1][a-1] = c

ans = 0
for p in itertools.permutations(range(N)):
    l = 0

    now = p[0]
    for next in p[1:]:
        if next in g[now]:
            l += g[now][next]
            now = next
        else:
            break

    ans = max(ans,l)

print(ans)
