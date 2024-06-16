import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

N = int(input())
A = list(map(int,input().split()))

g = [[] for i in range(N)]
for i in range(N):
    a,b = i+1, A[i]
    g[a-1].append(b-1)
    

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0))
    visited = {}
    path = []
    while q:
        s,d = q.pop()
        if s in visited:
            path.append(s)
            break
        visited[s] = d
        path.append(s)
        for t in g[s]:
            q.append((t,d+1))
    return visited,path

visited, path = bfs(0)

visited = {}


ans = []
ind = path.index(path[-1])
for i in range(ind,len(path)-1):
    ans.append(path[i]+1)

print(len(ans))
print(*ans)