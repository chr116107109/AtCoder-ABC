
N,X,Y = map(int,input().split())
d = [[] for i in range(N)]
for i in range(N-1):
    U,V = map(int,input().split())
    d[U-1].append(V-1)
    d[V-1].append(U-1)

from collections import deque
from webbrowser import get
def dfs(d,X,Y):
    visited = {}
    q = deque()
    q.append([X,0])
    while q:
        s, dist = q.popleft()
        if s in visited:
            continue
        visited[s] = dist
        if s == Y:
            return visited
        for t in d[s]:
            q.append([t,dist+1])

def get_path(d,visited,X,Y):
    path = [Y]
    dist = visited[Y]
    t = Y
    while dist > 0:
        
        for s in d[t]:
            if s in visited:
                if visited[s] == dist - 1:
                    t = s
                    path.append(s)
                    dist -= 1
                    break
    path.reverse()
    return path


visited = dfs(d,X-1,Y-1)
ans = get_path(d,visited,X-1,Y-1)
print(*[a+1 for a in ans])