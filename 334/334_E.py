import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


H,W = map(int,input().split())

S = [list(input()) for _ in range(H)]

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

uf=UnionFind(H*W)

def f(i,j):
    return i*W+j

green_cout = 0

for i in range(H):
    for j in range(W):
        if i+1 < H and S[i][j] == S[i+1][j] and S[i][j] == "#":
            uf.union(f(i,j),f(i+1,j))
        if j+1 < W and S[i][j] == S[i][j+1] and S[i][j] == "#":
            uf.union(f(i,j),f(i,j+1))

        if S[i][j] == "#":
            green_cout += 1

mod = 998244353
inv = pow(H*W - green_cout,mod-2,mod)
#inv = 1/(H*W - green_cout )
ans = 0

group_count = uf.group_count() - (H*W - green_cout)

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            roots = set()
            for s,t in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= s < H and 0 <= t < W and S[s][t] == "#":
                    roots.add(uf.find(f(s,t)))

            if len(roots) > 1:
                ans += max(group_count - len(roots)+1,1) * inv
                ans %= mod
            elif len(roots) == 1:
                ans += (group_count) * inv
                ans %= mod
            else:
                ans += (group_count+1) * inv
                ans %= mod

            #print(i,j,ans,roots)

print(ans)