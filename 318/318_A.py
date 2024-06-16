import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M,P = map(int,input().split())

if N < M:
    print(0)
else:
    print((N-M)//P + 1)

