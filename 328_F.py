

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,Q = map(int,input().split())

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

INF = float('inf')
P = [INF] * N

ans = []
for i in range(Q):
    a,b,d = map(int,input().split())
    a -= 1
    b -= 1
    
    if a == b and d == 0:
        ans.append(i+1)
        continue
    if uf.same(a,b):
        if P[a] - P[b] != d:
            continue
        else:
            ans.append(i+1)
    else:
        ans.append(i+1)
        if uf.size(a) == uf.size(b) == 1:
            uf.union(a,b)
            if a == uf.find(a):
                P[a] = 0
                P[b] = -d
            else:
                P[b] = 0
                P[a] = d
        elif uf.size(a) == 1:
            uf.union(a,b)
            P[a] = P[b] + d
        elif uf.size(b) == 1:
            uf.union(a,b)
            P[b] = P[a] - d
        else:
            root_a = uf.find(a)
            grouo_a = uf.members(a)
            root_b = uf.find(b)
            grouo_b = uf.members(b)
            uf.union(a,b)
            if root_a == uf.find(a):
                for x in grouo_b:
                    P[x] -= d
            else:
                for x in grouo_a:
                    P[x] += d


print(*ans)