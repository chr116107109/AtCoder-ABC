
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,D,W = map(int,input().split())
d = defaultdict(list)
for i in range(N):
    t,x = map(int,input().split())  
    d[t].append(x)

f = []
keys = sorted(d.keys())
for x in keys:
    f.append([x,sorted(d[x])])


ind2value = [f[i][0] for i in range(len(f))]
g = {}

now = 0
