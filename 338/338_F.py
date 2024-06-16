import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

q = deque()

g = [[] for i in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    g[a-1].append([b-1,c])
    

INF = 10**18
d = [[INF] * (N) for i in range(2**N)]

d[0][0] = 0
for i in range(N):
    d[1<<i][i] = 0
    for j,c in g[i]:
        d[1<<j][j] = min(d[1<<j][j],c)

for bit in range(1,2**N):
    for i in range(N):
        for j,c in g[i]:
            if bit & (1<<j) != 0:
                continue
            if d[bit][i] == INF:
                continue
            d[bit | (1<<j)][j] = min(d[bit | (1<<j)][j],d[bit][i]+c)

if d[2**N-1][0] == INF:
    print('No')
else:
    print(min(d[2**N-1]))

