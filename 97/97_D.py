

N,M = map(int,input().split())
A = list(map(int,input().split()))

g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

from collections import deque
def bfs(s,visited):
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

visited = {}
ans = 0
for i in range(N):
    if not i in visited:
        v = bfs(i,{})
        for j in v.keys():
            if A[j]-1 in v:
                ans += 1
        visited.update(v)

print(ans)
