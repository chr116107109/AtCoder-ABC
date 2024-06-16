import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    a = []
    for j in range(N):
        if A[i][j] == 1:
            a.append(j+1)
    print(*a)