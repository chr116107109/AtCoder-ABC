import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,A =   map(int,input().split())

T = list(map(int,input().split()))

q = []

now = 0

T.sort()

for i in range(N):
    if i == 0:
        now = A
        print(T[i] + now)
    else:
        now -= T[i] - T[i-1]
        now = max(now,0)
        now += A
        print(T[i] + now)
