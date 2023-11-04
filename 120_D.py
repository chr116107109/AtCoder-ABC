
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
A = [list(map(int,input().split())) for i in range(M)]
A = A[::-1]

B = [0] * M
for i,[a,b] in enumerate(A):
    if uf.find(a-1) != uf.find(b-1):
        B[i] = uf.size(a-1) * uf.size(b-1)
        uf.union(a-1,b-1)

B = B[::-1]
for i in range(1,M):
    B[i] += B[i-1]

for b in B:
    print(b)
