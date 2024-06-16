
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

ans = 'No'
for a,b,c in itertools.combinations(A,3):
    dx1 = b[0] - a[0]
    dy1 = b[1] - a[1]
    dx2 = c[0] - a[0]
    dy2 = c[1] - a[1]

    if dx2 * dy1 == dx1 * dy2:
        ans = 'Yes'

print(ans)