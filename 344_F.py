import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

P = [list(map(int,input().split())) for _ in range(N)]
R = [list(map(int,input().split())) for _ in range(N)]
D = [list(map(int,input().split())) for _ in range(N-1)]

def f(i,j):
    return N*i+j

g = [[] for i in range(N*N)]
rg = [[] for i in range(N*N)]
for i in range(N):
    for j in range(N):
        
        if i < N-1:
            g[f(i,j)].append([f(i+1,j),D[i][j]])
            rg[f(i+1,j)].append([f(i,j),D[i][j]])
        if j < N-1:
            g[f(i,j)].append([f(i,j+1),R[i][j]])
            rg[f(i,j+1)].append([f(i,j),R[i][j]])

from heapq import heappush,heappop
def djkstra(s,g):
    q = []
    heappush(q,[0,s])
    visited = {}
    while q:
        d,s = heappop(q)
        if s in visited:
            continue
        visited[s] = d
        for [t,w] in g[s]:
            heappush(q,[d+w,t])
    return visited
    
dist_from = []
for i in range(N):
    for j in range(N):
        dist_from.append(djkstra(f(i,j),g))


q = []
heappush(q,[0,0,0])
visited = {}

while q:
    print(q)
    d,money,s = heappop(q)
    if (s,money) in visited:
        continue
    if s == N*N-1:
        print(d)
        break
    visited[(s,money)] = d
    
    for t,cost in dist_from[s].items():
        if s == t:
            continue
        i,j = s//N,s%N
        if money > cost:
            continue
        dist = -(- (cost - money) // P[i][j]) + (t//N-i) + (t%N-j)
        assert dist >= 1
        new_dist = d + dist
        new_money = money + P[i][j]*(dist-1) - cost
        #print([s//N,s%N],[t//N,t%N],dist, new_dist,new_money)
        heappush(q,(new_dist,new_money,t))

