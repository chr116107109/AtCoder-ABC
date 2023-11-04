
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A,B,C,D = map(int,input().split())

count = 0

while True:
    if count%2 == 0:
        C -= B
    else:
        A -= D
    count += 1
    if A <= 0:
        print('No')
        break
    if C <= 0:
        print('Yes')
        break