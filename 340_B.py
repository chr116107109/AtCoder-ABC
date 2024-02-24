import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A = []

Q = int(input())

for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        A.append(q[1])
    else:
        print(A[-q[1]])