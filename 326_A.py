import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

X,Y = map(int,input().split())

if X < Y-2 or X > Y + 3:
    print('No')
else:
    print('Yes')