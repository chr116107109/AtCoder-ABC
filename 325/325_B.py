import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

ans = 0
for i in range(24):
    score = 0
    for j in range(N):
        if 9<=(i+A[j][1])%24<=17:
            score += A[j][0]

    ans = max(ans,score)

print(ans)