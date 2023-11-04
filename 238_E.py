
N,Q = map(int,input().split())

g = [[] for i in range(N+1)]
for i in range(Q):
    a,b = map(int,input().split())
    g[a-1].append(b)
    g[b].append(a-1)

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

visited = bfs(0)

if N in visited:
    print('Yes')
else:
    print('No')


