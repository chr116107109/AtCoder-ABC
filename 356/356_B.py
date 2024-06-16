import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = list(map(int,input().split()))

for i in range(N):
    X = list(map(int,input().split()))
    for i in range(M):
        A[i] -= X[i]
        A[i] = max(0,A[i])

if A == [0] * M:
    print("Yes")
else:   
    print("No")