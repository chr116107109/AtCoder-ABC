import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]

ans = [[] for _ in range(N)]

for i in range(N):
    dist = 0
    ind = i
    for j in range(N):
        x = A[i]
        y = A[j]
        if i == j:
            continue
        if dist < (x[0] - y[0])**2 + (x[1] - y[1])**2:
            dist = (x[0] - y[0])**2 + (x[1] - y[1])**2
            ind = j

    ans[i] = ind+1


print(*ans,sep='\n')