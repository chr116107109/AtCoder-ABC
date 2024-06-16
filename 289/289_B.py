

N,M = map(int,input().split())
A = list(map(int,input().split()))

g = [[] for i in range(N)]
for i in range(M):
    a,b = A[i], A[i] + 1
    g[a-1].append(b-1)
    g[b-1].append(a-1)

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

all = set(range(N))
v = set()
ans = []
while len(v) < N:
    s = min(all-v)
    visited = bfs(s)
    visited = [[i,d] for i,d in visited.items()]
    visited.sort(key= lambda x: x[1])
    while visited:
        i,d = visited.pop()
        ans.append(i+1)
        v.add(i)

print(*ans)