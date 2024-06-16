
import sys

N,M = map(int,input().split())
g = [[] for i in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

from collections import deque
def bfs(s):
    visited = {}
    q = deque()
    q.append((s,0))

    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in g[s]:
            q.append((t,d+1))

    return visited

visited = bfs(0)
u,d = 0,-1
for s in visited:
    if d < visited[s]:
        d = visited[s]
        u = s

visited = bfs(u)
u,d = 0,-1
for s in visited:
    if d < visited[s]:
        d = visited[s]
        u = s

if d == N-1:
    print('Yes')
else:
    print('No')

