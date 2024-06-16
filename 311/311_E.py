import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


H,W,N = map(int,input().split())

hole_x = [[] for i in range(H)]
hole_y = [[] for i in range(W)]

B = set()
for i in range(N):
    a,b = map(int,input().split())
    hole_x[a-1].append(b-1)
    hole_y[b-1].append(a-1)
    B.add((a-1,b-1))


ans = 0
for i in range(H):
    for j in range(W):
        if (i,j) in B:
            continue
            
        if hole_x[i] == []:
            x = W-i+1
        