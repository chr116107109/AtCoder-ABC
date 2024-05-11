import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,X,Y,Z = map(int,input().split())

x,y = min(X,Y),max(X,Y)

if x <= Z <= y:
    print('Yes')
else:
    print('No')