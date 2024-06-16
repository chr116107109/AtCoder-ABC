import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
import functools
N = int(input())


@functools.lru_cache(maxsize=None)
def f(x,ans):
    if x < 2:
        return 0
    ans += x
    ans += f(x//2,0)
    ans += f(-(-x//2),0)
    return ans

print(f(N,0))