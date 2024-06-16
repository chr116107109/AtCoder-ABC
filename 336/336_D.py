import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
A = list(map(int,input().split()))


left = [0] * N

left[0] = 1

for i in range(1,N):
    if A[i] >= left[i-1] + 1:
        left[i] = left[i-1] + 1
    else:
        left[i] = min(left[i-1],A[i])

right = [0] * N
right[0] = 1
A = A[::-1]

for i in range(1,N):
    if A[i] >= right[i-1] + 1:
        right[i] = right[i-1] + 1
    else:
        right[i] = min(right[i-1],A[i])

right = right[::-1]

ans = 1
for i in range(N):
    ans = max(ans,min(left[i],right[i]))

print(ans)