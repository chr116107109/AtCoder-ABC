import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

d = [deque() for i in range(N+1)]

count = [0] * (N+1)
for i in range(N):
    if len(d[A[i]]) == 0:
        d[A[i]].append((i,0))
    else:
        d[A[i]].append((i,d[A[i]][-1][1] + i - d[A[i]][-1][0] - 1))
        count[A[i]] += d[A[i]][-1][1]
ans = 0

#print(d)
for i in range(N):
    #print(ans)
    if len(d[A[i]]) > 1:
        ind, c = d[A[i]].popleft()

        ans += count[A[i]] - c*(len(d[A[i]])+1)
        count[A[i]] -= c
print(ans)