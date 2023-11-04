
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

D,G = map(int,input().split())
G //= 100
A = [list(map(int,input().split())) for i in range(D)]

inf = 10**10
d = [[inf] * (G+1) for i in range(D+1)]
d[0][0] = 0

for i in range(D):

    for j in range(G+1):

        s, p, c = i+1, A[i][0], A[i][1]
        c //= 100
        for k in range(p):
            d[i+1][min(G,j+k*s)] = min(d[i+1][min(G,j+k*s)], d[i][j]+k)
        d[i+1][min(G,j+p*s+c)] = min(d[i+1][min(G,j+p*s+c)], d[i][j]+p)

print(d[-1][-1])