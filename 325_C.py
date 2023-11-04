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


H,W = map(int,input().split())
S = [list(input()) for i in range(H)]
N = 0
d = {}
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            d[(i,j)] = len(d)
            N += 1

uf=UnionFind(N)

M = 100000


for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            continue
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                if 0<=i+x<H and 0<=j+y<W:
                    if S[i+x][j+y] == '#':
                        uf.union(d[i,j],d[i+x,j+y])

print(uf.group_count())