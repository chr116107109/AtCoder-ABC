
N,Q = map(int,input().split())
C = list(map(int,input().split()))

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

from collections import Counter
d = [{} for i in range(N)]
for i in range(N):
    d[i][C[i]] = 1

for i in range(Q):
    q = list(map(int,input().split()))
    q[1] -= 1
    q[2] -= 1

    if q[0] == 1:
        if uf.find(q[1]) != uf.find(q[2]):
            xp = uf.find(q[1])
            xc = d[uf.find(q[1])]
            yp = uf.find(q[2])
            yc = d[uf.find(q[2])]
            uf.union(q[1],q[2])
            new_parent = uf.find(q[1])
            if new_parent == xp:
                for c in yc:
                    if c in d[new_parent]:
                        d[new_parent][c] += yc[c]
                    else:
                        d[new_parent][c] = yc[c]
            else:
                for c in xc:
                    if c in d[new_parent]:
                        d[new_parent][c] += xc[c]
                    else:
                        d[new_parent][c] = xc[c]

    if q[0] == 2:
        if q[2]+1 in d[uf.find(q[1])]:
            print(d[uf.find(q[1])][q[2]+1])
        else:
            print(0)
