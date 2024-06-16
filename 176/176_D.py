from collections import deque

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

H,W = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

S = [input() for i in range(H)] 

uf=UnionFind(H*W)

def f(s):
    return s[0]*W+s[1]
def bfs(s):
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        for d in [[-1,0],[1,0],[0,1],[0,-1]]:
            t = [s[0]+d[0],s[1]+d[1]]
            if 0 <= t[0] < H and 0<= t[1] < W:
                if S[t[0]][t[1]] == '.' and uf.find(f(s)) != uf.find(f(t)):
                    q.append(t)
                    uf.union(f(s),f(t))


root_to_ind = {}
ind_to_root = {}
n_component = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.' and uf.size(f([i,j])) == 1:
            bfs([i,j])
            root = uf.find(f([i,j]))
            root_to_ind[root] = n_component
            ind_to_root[n_component] = root
            n_component += 1


g = [set() for i in range(n_component)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            root = uf.find(f([i,j]))
            ind = root_to_ind[root]
            for ii in range(-2,3):
                for jj in range(-2,3):
                    t = [i+ii,j+jj]
                    if 0 <= t[0] < H and 0<= t[1] < W:
                        if S[t[0]][t[1]] == '.' and uf.find(f([i,j])) != uf.find(f(t)):
                            g[ind].add(root_to_ind[uf.find(f(t))])
                            g[root_to_ind[uf.find(f(t))]].add(ind)

start = root_to_ind[uf.find(f([A[0]-1,A[1]-1]))]
goal = root_to_ind[uf.find(f([B[0]-1,B[1]-1]))]


visited = {}
q = deque()
q.append([start,0])

while q:
    s,d = q.popleft()
    if s in visited:
        continue
    visited[s] = d
    for t in g[s]:
        q.append([t,d+1])

if goal in visited:
    print(visited[goal])
else:
    print(-1)