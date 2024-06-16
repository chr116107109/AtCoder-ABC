import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = list(map(int,input().split()))

ans = []
for i in range(N):
    ans.append(0)
    for j in range(7):
        ans[-1] += A[i*7+j]

print(*ans)