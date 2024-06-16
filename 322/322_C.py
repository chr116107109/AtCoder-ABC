
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
A = list(map(int,input().split()))

B = [-1] * N
ind = M-1
for i in range(N-1,-1,-1):
    B[i] = A[ind]
    if i == A[ind-1]:
        ind -= 1

for i in range(N):
    print(B[i] - (i+1))

