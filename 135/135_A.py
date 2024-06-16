
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

if abs(N-M)%2 == 0:
    print(abs(N-M)%2)
else:
    print('IMPOSSIBLE')