
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
        group_members = defaultdict(set)
        for member in range(self.n):
            group_members[self.find(member)].add(member)
        return group_members

N,M,K = map(int,input().split())
uf_friend=UnionFind(N)
friend = [set() for i in range(N)]
block=[set() for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    uf_friend.union(a-1,b-1)
    friend[a-1].add(b-1)
    friend[b-1].add(a-1)
for i in range(K):
    a,b = map(int,input().split())
    block[a-1].add(b-1)
    block[b-1].add(a-1)


members = uf_friend.all_group_members()

ans = [0] * N
for root in members:
    mem = members[root]
    for m in mem:
        a = len(members[root]) - 1
        for b in friend[m]:
            if b in mem:
                a -= 1
        for b in block[m]:
            if b in mem:
                a -= 1

        ans[m] = a
print(*ans)