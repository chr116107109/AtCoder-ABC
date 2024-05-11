import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]  

M = sum([a[0] for a in A])

ans = 0

for i in range(N):
    ans = max(ans, M - A[i][0] + A[i][1])

print(ans)