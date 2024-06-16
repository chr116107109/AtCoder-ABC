

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M,K = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

d = [-1] * N
q = []

for i in range(K):
    p,h = map(int,input().split())
    heappush(q,(-h,p-1))

while q:
    #print(q)
    v,s = heappop(q)
    if d[s] != -1:
        continue

    d[s] = -v
    if v == 0:
        continue
    for t in g[s]:
        heappush(q,(v+1,t))

ans = []
for i in range(N):
    if d[i] >= 0:
        ans.append(i+1)

print(len(ans))
print(*ans)



