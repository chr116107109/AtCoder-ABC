
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,W = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]

d = [defaultdict(lambda:0) for i in range(N+1)]
d[0][0] = 0

for i in range(N):
    w,v = A[i]
    for x,y in d[i].items():
        d[i+1][x] = max(d[i+1][x], y)
        if w + x > W:
            continue
        
        d[i+1][min(W,w+x)] = max(d[i+1][min(W,w+x)], y+v)
        

print(max(d[-1].values()))