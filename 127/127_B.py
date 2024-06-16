
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

r,D,x = map(int,input().split())

for i in range(10):
    x = r*x - D
    
    print(x)
