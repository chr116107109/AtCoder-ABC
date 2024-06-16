import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
A = list(map(int,input().split()))

E = sum(A)//N

p = 0
m = 0
for i in range(N):
    if A[i] > E+1:
        p += A[i] - E - 1
    else:
        m += E - A[i]

print(max(p,m))