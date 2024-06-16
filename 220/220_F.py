
import sys
sys.setrecursionlimit(10**6)

N = int(input())
g = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

childs = [0] * N
dist = [0] * N
visited = set()
def dfs(s,d):
    if len(g[s]) == 1 and g[s][0] in visited:
        dist[s] = d
        childs[s] = 1 
        return 1
    
    visited.add(s)
    dist[s] = d
    c = 1
    for t in g[s]:
        if t in visited:
            continue
        c += dfs(t,d+1)
    childs[s] = c

    return c

dfs(0,0)

now = sum(dist)
ans = [0] * N
ans[0] = now
from collections import deque
def bfs(s):
    q = deque()
    q.append((s,now))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in g[s]:
            if t in visited:
                continue
            ans[t] = d - 2*childs[t] + N
            q.append((t,ans[t]))
    return visited

bfs(0)
print(*ans,sep='\n')