import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())

if N < 1000:
    print(N)
else:
    S = str(N)
    n = len(S)
    print(S[:3]+'0'*(n-3))