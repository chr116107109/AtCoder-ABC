import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,T = map(int,input().split())

d = defaultdict(set)

for i in range(N):
    d[0].add(i)

pos = [0] * N

for i in range(T):
    a,b = map(int,input().split())
    
    p = pos[a-1]
    d[p].remove(a-1)
    d[p+b].add(a-1)
    pos[a-1] += b
    if len(d[p]) == 0:
        del d[p]
    print(len(d))