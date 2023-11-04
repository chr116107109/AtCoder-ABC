import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


S = list(input())
N = len(S)

d = [[0] * (N+1) for i in range(N+1)]
mod=998244353
d[0][0] = 1
for i in range(1,N+1):
    for j in range(N+1):
        
        if S[i-1] == '(' and j < N:
            d[i][j+1] += d[i-1][j]
            d[i][j+1] %= mod
        if S[i-1] == ')' and j > 0:
            d[i][j-1] += d[i-1][j]
            d[i][j-1] %= mod
        if S[i-1] == '?':
            if j < N:
                d[i][j+1] += d[i-1][j]
                d[i][j+1] %= mod
            if j > 0:
                d[i][j-1] += d[i-1][j]
                d[i][j-1] %= mod

    
print(d[-1][0])