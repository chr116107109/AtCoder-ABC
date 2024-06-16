import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

q  = []

ans = 0

for i in range(M):
    b = B.pop()
    while A and b <= A[-1]:
        q.append(A.pop())

    if not q:
        ans = -1
        break

    ans += q.pop()

print(ans)

