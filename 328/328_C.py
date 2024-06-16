import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,Q = map(int,input().split())
S = list(input())

A = [0]
for i in range(1,N):
    A.append(A[-1])
    if S[i-1] == S[i]:
        A[-1] += 1

for i in range(Q):
    l,r = map(int,input().split())
    print(A[r-1] - A[l-1])