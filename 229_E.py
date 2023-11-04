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
g = [[] for i in range(N)]

for i in range(M):
    A,B = map(int,input().split())
    A,B = min(A,B), max(A,B)
    g[A-1].append(B-1)

uf=UnionFind(N)
ans = [0]
k = 0
for i in range(N-1,0,-1):
    k += 1
    for t in g[i]:
        if uf.find(i) != uf.find(t):
            k -= 1
            uf.union(i,t)
    ans.append(k)

for a in ans[::-1]:
    print(a)