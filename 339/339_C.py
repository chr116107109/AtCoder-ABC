import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

now = 0
min_now = 0
for i in range(N):
    now += A[i]
    min_now = min(min_now,now)

print(now-min_now)