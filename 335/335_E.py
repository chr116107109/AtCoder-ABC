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
uf=UnionFind(N)
A = list(map(int,input().split()))

g = [set() for i in range(N)]
E = []
for i in range(M):
    a,b = map(int,input().split())
    E.append([a-1,b-1])
    if A[a-1] == A[b-1]:
        uf.union(a-1,b-1)

for i in range(M):
    a,b = E[i]
    x,y = uf.find(a),uf.find(b)
    if x != y:
        if A[x] < A[y]:
            g[x].add(y)
        else:
            g[y].add(x)
h = []
heappush(h,(A[0],uf.find(0)))

dist = [0]*N
dist[0] = 1
count = 0
visited = [False]*N
while h:
    count += 1
    #print(h)
    d,i = heappop(h)
    if visited[i]:
        continue
    visited[i] = True
    #print(dist)
    for j in g[i]:
        heappush(h,(A[j],j))
        dist[j] = max(dist[i]+1,dist[j])
        
print(dist[uf.find(N-1)])