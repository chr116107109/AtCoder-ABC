
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right

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

N,Q = map(int,input().split())


g = [set() for i in range(N)]

iso_v = N
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        u,v = q[1]-1,q[2]-1

        if len(g[u]) == 0:
            iso_v -= 1
        g[u].add(v)

        if len(g[v]) == 0:
            iso_v -= 1
        g[v].add(u)

    if q[0] == 2:
        u = q[1]-1

        if len(g[u]) > 0:
            iso_v += 1

        for v in g[u]:
            g[v].remove(u)
            if len(g[v]) == 0:
                iso_v += 1
        
        g[u] = set()
        

    print(iso_v)