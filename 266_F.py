

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

N = int(input())
uf=UnionFind(N)
g = [[] for i in range(N)]
for i in range(N):
    a,b = map(int,input().split())
    if uf.find(a-1) != uf.find(b-1):
        g[a-1].append(b-1)
        g[b-1].append(a-1)
        uf.union(a-1,b-1)
    else:
        start,goal = a-1,b-1


from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in g[s]:
            q.append((t,d+1))
    return visited
def get_path(start,goal,visited):
    now = goal
    path = [goal]
    while now != start:
        for t in g[now]:
            if visited[t] == visited[now] - 1:
                path.append(t)
                now = t
                break
    
    path.reverse()
    return path

visited = bfs(start)
loop = get_path(start,goal,visited)

for i in range(len(loop)):
    if i > 0:
        g[loop[i]].remove(loop[i-1])
    if i < len(loop)-1:
        g[loop[i]].remove(loop[(i+1)%len(loop)])

uf = UnionFind(N)
for s in loop:
    q = deque()
    q.append(s)
    visited = set()
    while q:
        s = q.popleft()
        if s in visited:
            continue
        visited.add(s)
        for t in g[s]:
            q.append(t)
            uf.union(s,t)

Q = int(input())

for i in range(Q):
    a,b = map(int,input().split())
    if uf.find(a-1) != uf.find(b-1):
        print('No')
    else:
        print('Yes')