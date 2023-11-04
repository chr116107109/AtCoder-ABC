import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())

ans = []
for i in range(N+1):
    ok = False
    for j in range(1,10):
        if N%j == 0 and i%(N//j) == 0:
            ans.append(str(j))
            ok = True
            break
    if not ok:
        ans.append('-')

print("".join(ans))