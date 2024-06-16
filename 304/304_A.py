import sys
import math
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools


N = int(input())
A = [input().split() for i in range(N)]

n,v = 0,10**10
for i in range(N):
    if v > int(A[i][1]):
        n = i
        v = int(A[i][1])

for i in range(N):
    print(A[(n+i)%N][0])

