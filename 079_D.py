

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


H,W = map(int,input().split())

d = [[10**20]*10 for i in range(10)]
for i in range(10):
    c = list(map(int,input().split()))
    for j in range(10):
        d[i][j] = c[j]

def WFM(d,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])                    

    return d
    
d = WFM(d,10)

ans = 0
for i in range(H):
    A = list(map(int,input().split()))

    for j in range(W):
        if A[j] >= 0:
            ans += d[A[j]][1]

print(ans)