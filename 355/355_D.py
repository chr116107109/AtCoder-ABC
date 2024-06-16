import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())

A = [list(map(int,input().split())) for _ in range(N)]

B = []

for i in range(N):
    l,r = A[i]
    B.append([l,0])
    B.append([r,1])

B.sort(key=lambda x:x[0]*10 + x[1])

ans = 0
count = 0

for i in range(2*N):
    if B[i][1] == 0:
        count += 1
    else:
        count -= 1
        ans += count

print(ans)