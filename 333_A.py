import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
ans = ''
for i in range(N):
    ans += str(N)

print(ans)