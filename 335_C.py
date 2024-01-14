import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,Q = map(int,input().split())

trace = []
now = [1,0]
for i in range(1,N+1):
    trace.append([i,0])
trace.reverse()
ans = []
for i in range(Q):
    q = input().split()
    if q[0] == "1":
        if q[1] == 'L':
            now[0] -= 1
        if q[1] == 'R':
            now[0] += 1
        if q[1] == 'U':
            now[1] += 1
        if q[1] == 'D':
            now[1] -= 1
        trace.append(now[:])

    if q[0] == "2":
        p = int(q[1])
        ans.append(trace[-p])

for a in ans:
    print(*a)   