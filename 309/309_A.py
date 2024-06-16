import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


A,B = map(int,input().split())

A,B = min(A,B),max(A,B)

if A+1 == B and (A-1)//3 == (B-1)//3:
    print('Yes')
else:
    print('No')