import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A,B = map(int,input().split())

x = [1,2,3]

x.remove(A)
if B in x:  
    x.remove(B)

if len(x) == 1:
    print(x[0])
else:
    print(-1)