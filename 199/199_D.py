

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


N,M = map(int,input().split())
g = [[] for i in range(N)]
edges = []
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    edges.append([a-1,b-1])

from collections import deque
def bfs(s,visited,target):
    q = deque()
    q.append((s,0))
    visited[s] = 0
    ok = True
    while q:
        s,d = q.popleft()
        if not ok:
            break
        for t in g[s]:
            if not t in target:
                continue
            if not t in visited:
                q.append((t,(d+1)%2))
                visited[t] = (d+1)%2
            else:
                if visited[t] == visited[s]:
                    ok = False
                    break
    return visited,ok


ans = 0
for i in range(2**N):
    red = set()
    blue = set()
    for j in range(N):
        if i&(1<<j) != 0:
            red.add(j)
        else:
            blue.add(j)
    
    red_ok = True
    for s in red:
        if not red_ok:
            break
        for t in g[s]:
            if t in red:
                red_ok = False
    if not red_ok:
        continue
    visited = {}
    blue_ok = True
    uf=UnionFind(2*N)
    for s,t in edges:
        if s in blue and t in blue:
            uf.union(s,N+t)
            uf.union(t,N+s)

    for i in blue:
        if uf.find(i) == uf.find(N+i):
            blue_ok = False
        
    #print(i)
    #print(red_ok,blue_ok,uf.all_group_members())
    if red_ok and blue_ok:
        ans += pow(2,(uf.group_count())//2-len(red))

print(ans)