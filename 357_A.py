import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = list(map(int,input().split()))

for i in range(N+1):
    if i == N or A[i] > M:
        print(i)
        break
    M -= A[i]

