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
for i in range(100):
    for j in range(100):
        x = i+0.5
        y = j+0.5
        ok = False
        for a in A:
            if a[0] <= x <= a[1] and a[2] <= y <= a[3]:
                ok = True
                break
        if ok :
            ans += 1

print(ans)