import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

edges = []

for _ in range(M):
    k,c = map(int,input().split())
    a = list(map(int,input().split()))
    edges.append([c,a])

edges.sort(key=lambda x:x[0])

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

uf=UnionFind(N+1)

ans = 0

c, a = edges[0]
for i in range(1,len(a)):
    uf.union(a[i-1],a[i])
    ans += c

for c,a in edges:
    for i in range(len(a)):
        if uf.same(a[i-1],a[i]):
            continue
        uf.union(a[i-1],a[i])
        ans += c

if uf.group_count() == 2:
    print(ans)
else:
    print(-1)