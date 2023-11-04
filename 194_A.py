import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A,B = map(int,input().split())

A = A+B
if A>=15 and B>=8:
    print(1)
elif A>=10 and B>=3:
    print(2)
elif A>=3:
    print(3)
else:
    print(4)