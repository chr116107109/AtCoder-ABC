


import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())
A,B,C = map(int,input().split())

g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

visited = set()
ans = 'No'
def dfs(s):
    if s in visited:
        return
    global ans
    if s == C-1 and B-1 in visited:
        ans = 'Yes'
    visited.add(s)
    for t in g[s]:
        dfs(t)
    
    visited.remove(s)

dfs(A-1)
print(ans)