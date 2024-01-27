import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

B = [-1] * N
for i in range(N):
    if A[i] == -1:
        now = i
        continue

    B[A[i]-1] = i

ans = []
for i in range(N):
    ans.append(now+1)
    now = B[now]

print(*ans)
