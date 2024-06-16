import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())

if N%5 < 3:
    print(N-N%5)
else:
    print(N+5-N%5)
    