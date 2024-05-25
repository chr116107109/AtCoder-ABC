import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H = int(input())

x = 0
d = 1
while H > x:
    x += pow(2,d)
    d += 1

print(d)