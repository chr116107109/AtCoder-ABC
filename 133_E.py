
N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)


mod = 10**9+7

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0,M))
    visited = {}
    while q:
        s,d,ans = q.popleft()
        if s in visited:
            continue
        visited[s] = (d,ans)
        m = M-len(g[s])
        for t in g[s]:
            ans *= m
            ans %= mod
            m -= 1
            m = max(m,0)
        for t in g[s]:
            q.append((t,d,ans))
    return visited

visited = bfs(0)