import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,H,X = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    if H+A[i] >= X:
        print(i+1)
        break