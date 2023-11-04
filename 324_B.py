import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())

while N%2 == 0:
    N //= 2
while N%3 == 0:
    N //= 3

if N == 1:
    print('Yes')
else:
    print('No')