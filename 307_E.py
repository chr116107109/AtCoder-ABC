import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())
mod=998244353

d = [[0,0] for i in range(N)]
d[0] = [M,0]
for i in range(1,N):
    d[i][0] += d[i-1][1]
    d[i][0] %= mod
    d[i][1] += d[i-1][0]*(M-1)+d[i-1][1]*(M-2)
    d[i][1] %= mod

print(d[-1][1])