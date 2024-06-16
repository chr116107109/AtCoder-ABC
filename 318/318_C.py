import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,D,P = map(int,input().split())

A = list(map(int,input().split()))

A.sort(reverse=True)
B = [0]
for i in range(N):
    B.append(B[-1]+A[i])

now = 0

ans = 0
d = 0
while now < N:

    if d > 0:
        d -= 1
    else:
        if B[min(now+D,N)] - B[now] > P:
            d = D-1
            ans += P
        else:
            ans += A[now]

    now += 1

print(ans)