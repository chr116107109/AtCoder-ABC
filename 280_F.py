

from collections import deque
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

N,M,Q = map(int,input().split())
uf=UnionFind(N)
g = [[] for i in range(N)]

for i in range(M):
    A,B,C = map(int,input().split())
    g[A-1].append([B-1,C])
    g[B-1].append([A-1,-C])
    uf.union(A-1,B-1)

Bad = set()
def bfs(s):
    q = deque()
    q.append([s,0])
    inf_flag = False
    while q:
        s,d = q.popleft()
        if visited[s] < inf:
            if visited[s] != d:
                inf_flag = True
                break
            continue
        visited[s] = d
        for t,c in g[s]:
            q.append([t,d+c])

    if inf_flag:
        Bad.add(uf.find(s))

inf = 10**20
visited = [inf]*N
for i in range(N):
    if visited[i] == inf:
        bfs(i)


for _ in range(Q):
    X,Y = map(int,input().split())
    if uf.find(X-1) != uf.find(Y-1):
        print('nan')
    elif uf.find(X-1) in Bad:
        print('inf')
    else:
        print(visited[Y-1]-visited[X-1])