import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math



N = int(input())

g = [[] for i in range(N)]
for i in range(N-1):
    a,b,c = map(int,input().split())
    g[i].append([i+1,a])
    g[i].append([c-1,b])


q = []
heappush(q,(0,0))
visited = {}

while q:
    d,s = heappop(q)
    if s in visited:
        continue
    visited[s] = d
    for i in g[s]:
        heappush(q,(d+i[1],i[0]))

print(visited[N-1])