
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
P = list(map(int,input().split()))
g = [[] for i in range(N)]
for i in range(N-1):
    a,b = i+1, P[i] - 1
    g[a].append(b)
    g[b].append(a)

visited = {}
ot = []
inout = [[0,0] for i in range(N)]
def dfs(s,d):
    if len(g[s]) == 1 and s != 0:
        visited[s] = d
        inout[s][0] = len(ot)
        ot.append(s)
        inout[s][1] = len(ot)
        ot.append(s)
        return
    
    visited[s] = d
    inout[s][0] = len(ot)
    ot.append(s)
    for t in g[s]:
        if t in visited:
            continue
        dfs(t,d+1)
    inout[s][1] = len(ot)
    ot.append(s)

    return

dfs(0,0)

dist2ind = [[] for i in range(N)]
for i,s in enumerate(ot):
    dist2ind[visited[s]].append(i) 


Q = int(input())

for i in range(Q):
    u,d = map(int,input().split())

    s,t = inout[u-1]
    
    l = bisect_left(dist2ind[d],s)
    r = bisect_left(dist2ind[d],t)

    #print(s,t,l,r)
    
    print((r-l+1)//2)