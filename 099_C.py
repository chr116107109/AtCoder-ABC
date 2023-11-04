import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

d = [0] * (N+1)
for i in range(1,N+1):
    d[i] = i

p = 6
while p <= N:
    for i in range(N+1):
        if i+p <= N:
            d[i+p] = min(d[i+p],d[i]+1)

    p *= 6

p = 9
while p <= N:
    for i in range(N+1):
        if i+p <= N:
            d[i+p] = min(d[i+p],d[i]+1)
    
    p *= 9

print(d[-1])