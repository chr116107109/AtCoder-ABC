

from collections import defaultdict
from re import I

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


N,Q = map(int,input().split())


uf = UnionFind(N+Q+1)
M = N
ball2box = [-1] * (N+Q+1)
box2ball = [[-1,0] for i in range(N)] #box to (代表元,size)
for i in range(N):
    ball2box[i] = i
    box2ball[i] = [i,1]
ans = []
for _ in range(Q):
    q = list(map(int,input().split()))
    #print(' ')
    #print(q)
    if q[0] == 1:
        X,Y = q[1],q[2]
        [repX,sizeX] = box2ball[X-1]
        [repY,sizeY] = box2ball[Y-1]
        if sizeX == 0 and sizeY == 0:
            continue
        elif sizeX == 0:
            ball2box[repY] = X-1
            box2ball[X-1] = [repY,sizeY]
            box2ball[Y-1] = [-1,0]
        elif sizeY > 0:
            uf.union(repX,repY)
            ball2box[repY] = X-1
            box2ball[X-1] = [uf.find(repX),sizeY+sizeX]
            box2ball[Y-1] = [-1,0]
    if q[0] == 2:
        X = q[1]
        if box2ball[X - 1][1] == 0:
            box2ball[X - 1] = [M,1]
            ball2box[M] = X-1
        else:
            uf.union(box2ball[X-1][0],M)
            box2ball[X-1][1] += 1
        M += 1
    if q[0] == 3:
        ans.append(ball2box[uf.find(q[1]-1)]+1)

    #print(uf.parents)
    #print(ball2box)
    #print(box2ball)
    

for a in ans:
    print(a)