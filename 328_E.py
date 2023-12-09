import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
from itertools import combinations, product
from collections import namedtuple

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

N,M,K = map(int,input().split())

edge = []
weight = []
for i in range(M):
    a,b,w = map(int,input().split())
    edge.append((a-1,b-1,w))
    weight.append(w)

INF = float('inf') 
ans = INF

for e in itertools.combinations(edge,N-1):
    uf=UnionFind(N)
    #print(e)
    score = 0
    for a,b,w in e:
        uf.union(a,b)
        score += w
        score %= K

    if uf.group_count() == 1:
        ans = min(score,ans)

print(ans)