

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A = list(map(int,input().split()))

ans = 0
i = 0
for a in A:
    ans += A[i]*pow(2,i)
    i += 1

print(ans)