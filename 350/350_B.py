import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,Q = map(int,input().split())

T = list(map(int,input().split()))  

A = [1] * N

for i in range(Q):
    t = T[i]
    A[t-1] += 1
    A[t-1] %= 2

print(sum(A))