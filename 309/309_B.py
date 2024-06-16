import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
import copy
N = int(input())
A = [list(input()) for i in range(N)]
B = copy.deepcopy(A)

for i in range(1,N):
    B[0][i] = A[0][i-1]
for i in range(1,N):
    B[i][-1] = A[i-1][-1]
for i in range(N-2,-1,-1):
    B[-1][i] = A[-1][i+1]
for i in range(N-2,-1,-1):
    B[i][0] = A[i+1][0]

for i in range(N):
    print("".join(B[i]))