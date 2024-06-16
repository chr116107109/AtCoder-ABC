import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools

N,M = map(int,input().split())

A = [list(map(int,input().split())) for i in range(M)]

ans = N*(N-1)//2

d = set()

for i in range(M):
    for j in range(N-1):
        x,y = min(A[i][j],A[i][j+1]),max(A[i][j],A[i][j+1])
        if (x,y) in d:
            continue
        else:
            d.add((x,y))
            ans -= 1

print(ans)