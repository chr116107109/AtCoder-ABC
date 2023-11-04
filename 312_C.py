
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

l = 0
r = 10**10

while l < r:
    #print(l,r)
    m = (l+r)//2

    n_s = 0
    n_b = 0
    for i in range(N):
        if A[i] <= m:
            n_s += 1
    for i in range(M):
        if B[i] >= m:
            n_b += 1

    if n_s >= n_b:
        r = m 
    else:
        l = m + 1

print(l)
