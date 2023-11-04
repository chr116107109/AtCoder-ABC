from collections import defaultdict
from operator import is_

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


    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())



N,M = map(int,input().split())
edges = [list(map(int,input().split())) for i in range(M)]

def is_bridge(k):
    uf = UnionFind(N)
    for i in range(M):
        if i == k:
            continue
        uf.union(edges[i][0]-1,edges[i][1]-1)
    
    return uf.group_count() > 1

ans = 0
for i in range(M):
    if is_bridge(i):
        ans += 1
print(ans)
