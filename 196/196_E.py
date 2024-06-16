

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

T = []
A = []
for i in range(N):
    a,t = map(int,input().split())
    A.append(a)
    T.append(t)

Q = int(input())
X = list(map(int,input().split()))

inf = 10**20
interval = [-inf, inf]
bot,top = -inf,inf
mid = 0
for i in range(N):
    a,t = A[i],T[i]
    if t == 1:
        interval[0] = min(interval[0],interval[0]+a)
        interval[1] = max(interval[1],interval[1]+a)
        mid += a
        bot += a
        top += a
    if t == 2:
        interval[0] = max(a-mid,interval[0])
        bot = max(bot,a)
        top = max(top,a)
    if t == 3:
        interval[1] = min(a-mid,interval[1])
        bot = min(bot,a)
        top = min(top,a)


    #print(a,t)
    #print(interval)
for i in range(Q):
    if interval[0] < X[i] < interval[1]:
        print(X[i]+mid)
    elif X[i] <= interval[0]:
        print(bot)
    elif X[i] >= interval[1]:
        print(top)
    