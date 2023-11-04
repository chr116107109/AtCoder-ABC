import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,H = map(int,input().split())

X = list(map(int,input().split()))
X = [0] + X
A = [list(map(int,input().split())) for i in range(N-1)]

inf = 100
d = [[inf]*(H+1) for i in range(2*N)]

d[0][H] = [0,0]

for i in range(N):
    for j in range(H+1):
        for k in range(i+1,N):
            if X[k]-X[i] < j:
                continue
            p,f = A[i]
            d[k][j - (X[k]- X[i])] = min(d[k][j - (X[k]- X[i])], d[i][j])

            d[k][min(j - (X[k]- X[i]) + f,H)] = min(d[k][min(j - (X[k]- X[i]) + f,H)], d[i][j]+p)
        for k in range(N):
            dist = X[N-k]-X[i]
            if dist < j:
                continue
            p,f = A[N-k-1]
            d[N+N-k][j - dist] = min(d[k][j - dist], d[i][j])

            d[k][min(j - (X[k]- X[i]) + f,H)] = min(d[k][min(j - (X[k]- X[i]) + f,H)], d[i][j]+p)
        