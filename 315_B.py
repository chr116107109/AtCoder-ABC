import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = [list(map(int,input().split())) for i in range(N)]

A.sort(key=lambda x:x[1])

ans = A[-1][1]

x = A[-1][0]

a = 0
for i in range(N-1):
    if A[i][0] == A[-1][0]:
        a = max(a,A[i][1]//2)
    else:
        a = max(a,A[i][1])

print(ans+a)