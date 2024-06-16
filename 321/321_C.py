import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

K = int(input())

q = list(range(10))

T = set()
visited = set()
while q:
    #print(q)
    s = q.pop()
    if s in visited:
        continue
    visited.add(s)
    n = len(str(s))
    if s//(10**(n-1)) == 9:
        continue
    for t in range(s//(10**(n-1))+1,10):
        q.append((10**n)*t + s)

T = sorted(list(visited))

print(T[K])