import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A,B  = map(int,input().split())

for i in range(10):
    if i != A+B:
        print(i)
        break   