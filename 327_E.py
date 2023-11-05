import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())

A = list(map(int,input().split()))

INF=float('inf')
d = [[-INF]*(N+1) for _ in range(N+1)]

d[0][0] = 0
for i in range(1,N+1):
    d[i][0] = 0
    for j in range(1,i+1):
        d[i][j] = max(d[i][j],d[i-1][j-1]*0.9 + A[i-1],d[i-1][j])

ans = -INF
M = 1
for i in range(1,N+1):
    score = d[-1][i] / M
    score -= 1200/math.sqrt(i)
    ans = max(ans,score)
    #print(d[-1][i],score,M)
    M = M*0.9 + 1  
print(ans)