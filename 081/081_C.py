
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())
A = list(map(int,input().split()))

d = Counter()
for i in range(N):
    d[A[i]] += 1

d = list(d.items())
d.sort(key=lambda x:x[1])
ans = 0

if len(d) - K <= 0:
    print(0)
else:
    for i in range(len(d)-K):
        ans += d[i][1]

    print(ans)


