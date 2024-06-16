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


    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())



N = int(input())
XY = [list(map(int,input().split())) for i in range(N)]

M = 10**3
L = 10**4
uf = UnionFind(len(XY))

def to_one(x,y,M,L):
    return L*(x+M) + (y+M)

f = {}
for i,[x,y] in enumerate(XY):
    f[to_one(x,y,M,L)] = i

round = {}
import itertools
for [x,y] in XY:
    if to_one(x,y,M,L) in round:
        for key in round[to_one(x,y,M,L)]:
            uf.union(f[to_one(x,y,M,L)],f[key])

    for [xx,yy] in [[x+1,y],[x,y+1],[x-1,y],[x,y-1],[x+1,y+1],[x-1,y-1]]:
        if not to_one(xx,yy,M,L) in round:
            round[to_one(xx,yy,M,L)] = {to_one(x,y,M,L)}
        else:
            round[to_one(xx,yy,M,L)].add(to_one(x,y,M,L))

print(uf.group_count())