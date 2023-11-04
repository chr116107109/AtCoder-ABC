

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

l = 0
r = 10**9+1

while l < r:
    #print(l,r)
    m = (l+r)//2

    B = [[0]*(N+1) for i in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):

            B[i][j] = B[i-1][j] + B[i][j-1] - B[i-1][j-1]
            if A[i-1][j-1] <= m:
                B[i][j] += 1

    possible = False
    for i in range(N+1-K):
        for j in range(N+1-K):
            count = B[i+K][j+K] - B[i+K][j] - B[i][j+K] + B[i][j]
            #print(count)
            border = K**2//2 if K%2==0 else K**2//2+1
            if count < border:
                continue
            else:
                possible = True
            

    if possible:
        r = m
    else:
        l = m + 1

print(l)


