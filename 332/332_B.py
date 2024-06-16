import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

K,G,M = map(int,input().split())

g,m = 0,0
for i in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        if g + m <=G:
            g += m
            m = 0   
        else:
            m -= G-g
            g = G

print(g,m)
