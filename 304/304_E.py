import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())

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

uf=UnionFind(N)

for i in range(M):
    u,v = map(int,input().split())
    uf.union(u-1,v-1)

g = [set() for i in range(N)]

K = int(input())
init = False
for i in range(K):
    x,y = map(int,input().split())
    u = uf.find(x-1)
    v = uf.find(y-1)
    if u == v:
        init = True
    g[u].add(v)
    g[v].add(u)


Q = int(input())

for i in range(Q):
    p,q = map(int,input().split())
    u = uf.find(p-1)
    v = uf.find(q-1)

    if v in g[u] or init:
        print('No')
    else:
        print('Yes')