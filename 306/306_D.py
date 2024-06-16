import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

inf = 10**20
d = [[-inf,-inf] for i in range(N+1)]
d[0] = [0,-inf]
for i in range(N):

    [X,Y] = A[i]
    
    if X == 1:
        d[i+1][0] = max(d[i][0],d[i+1][0])
        d[i+1][1] = max(d[i][1],d[i][0]+Y,d[i+1][1])
    else:
        d[i+1][0] = max(d[i][0],d[i][0]+Y,d[i][1]+Y,d[i+1][0])
        d[i+1][1] = max(d[i][1],d[i+1][1])

print(max(d[-1]))