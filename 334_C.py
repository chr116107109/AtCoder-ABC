import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())

A = list(map(int,input().split()))

ans = 0

if (2*N - K) % 2 == 0:
    for i in range(K//2):
        ans += A[2*i+1] - A[2*i]

    print(ans)
elif len(A) == 1:
    print(0)
else:
    B = [0]
    for i in range(K//2):
        B.append(B[-1] + A[2*i+1] - A[2*i])
    C = [0]
    for i in range(K//2):
        C.append(C[-1] + A[-2*i-1] - A[-2*i-2])

    ans = 10**10
    for i in range(len(B)):
        ans = min(ans,B[i] + C[-i-1])

    print(ans)