import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())

visited = set()
def dfs(s,par):
    v = input().split()
    #print(v)
    if v[0] == 'OK':
        sys.exit()
    v = list(map(int,v))
    visited.add(s)
    for t in v[1:]:
        if t in visited:
            continue
        print(t)
        dfs(t,s)
    
    print(par)
    _ = input().split()
    return

dfs(1,-1)