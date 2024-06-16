
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


p,q = input().split()

d = {'A':0,'B':3,'C':4,'D':8,'E':9,'F':14,'G':23}

a,b = d[p],d[q]
print(abs(a-b))