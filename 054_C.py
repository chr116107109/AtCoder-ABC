
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
g = [set() for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].add(b-1)
    g[b-1].add(a-1)

ans = 0
for p in itertools.permutations(range(N)):

    if p[0] != 0:
        continue
    ok = True
    for i in range(N-1):
        if not p[i+1] in g[p[i]]:
            ok = False
            break

    if ok:
        ans += 1

print(ans)