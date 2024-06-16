import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]

B = {}

for i in range(N):
    a,c = A[i]
    if c not in B:
        B[c] = a
    else:
        B[c] = min(B[c],a)

ans = 0
for k in B.keys():
    ans = max(ans,B[k])

print(ans)

