

N,M = map(int,input().split())

g = [[set(),set()] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1][0].add(b-1)
    g[b-1][1].add(a-1)

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
        for t in g[s][0]:
            q.append((t,d+1))
    return visited


ans = 0
for i in range(N):
    visited = bfs(i)
    ans += len(visited) - len(g[i][0]) - 1

print(ans)