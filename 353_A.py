import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = list(map(int,input().split()))

ans = -1
for i in range(1,N):
    if A[i] > A[0]:
        ans = i+1
        break

print(ans)