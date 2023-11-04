
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = [list(map(int,input().split())) for i in range(M)]
C = [list(map(int,input().split())) for i in range(N)]

ans = 10**20
d0 = Counter()
n0 = 0
d1 = Counter()
n1 = 0
d2 = Counter()
n2 = 0
for x in range(N):
    for y in range(N):
        if (x+y)%3 == 0:
            d0[C[x][y]] += 1
            n0 += 1
        if (x+y)%3 == 1:
            d1[C[x][y]] += 1
            n1 += 1
        if (x+y)%3 == 2:
            d2[C[x][y]] += 1
            n2 += 1

for i,j,k in itertools.permutations(range(M),3):
    score = 0
    
    for a in d1:
        score += A[a-1][i]*d1[a]
    for a in d2:
        score += A[a-1][j]*d2[a]
    for a in d0:
        score += A[a-1][k]*d0[a]

    ans = min(ans,score)
print(ans)