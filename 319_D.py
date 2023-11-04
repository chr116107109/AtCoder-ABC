import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
A = list(map(int,input().split()))

l = 0
r = 10**20

while l < r:
    #print(l,r,(l+r)//2)
    m = (l+r)//2

    d = [0] * M
    now = 0
    ok = True
    for i in range(N):
        if A[i] > m:
            ok = False
            break
        if d[now] + A[i] > m:
            now += 1
            if now == M:
                ok = False
                break
        d[now] += A[i] + 1
    
    #print(ok)
    #print(d)
    if ok:
        r = m
    else:
        l = m + 1

print(l)