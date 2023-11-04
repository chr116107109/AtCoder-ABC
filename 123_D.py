

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

X,Y,Z,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort(key=lambda x:-x)
B.sort(key=lambda x:-x)
C.sort(key=lambda x:-x)

q = []
heappush(q,[-(A[0]+B[0]+C[0]), 0,0,0])

visited = set()
for i in range(10**10):
    x,a,b,c = heappop(q)
    #print(q)
    if (a,b,c) in visited:
        continue
    visited.add((a,b,c))
    if a < X-1:
        heappush(q,[(x+A[a]-A[a+1]),a+1,b,c])
    if b < Y-1:
        heappush(q,[(x+B[b]-B[b+1]),a,b+1,c])
    if c < Z-1:
        heappush(q,[(x+C[c]-C[c+1]),a,b,c+1])

    print(-x)
    if len(visited) == K:
        break