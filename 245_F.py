

N,M = map(int,input().split())
g = [[set(),set()] for i in range(N)]
g_ori = [[set(),set()] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1][0].add(b-1)
    g[b-1][1].add(a-1)
    g_ori[a-1][0].add(b-1)
    g_ori[b-1][1].add(a-1)


def get_loop(g):
    q = []
    visited = set()
    for i in range(N):
        if g[i][1] == set():
            q.append(i)

    while q:
        s = q.pop()
        visited.add(s)
        for t in g[s][0]:
            g[t][1].remove(s)
            if g[t][1] == set():
                q.append(t)
    
    q = []
    for i in range(N):
        if g[i][0] == set():
            q.append(i)

    while q:
        s = q.pop()
        visited.add(s)
        for t in g[s][1]:
            g[t][0].remove(s)
            if g[t][0] == set():
                q.append(t)

    return visited

from collections import deque
def bfs(s,visited):
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        if s in visited:
            continue
        visited.add(s)
        for t in g_ori[s][1]:
            q.append(t)
    
    return visited


not_loop = get_loop(g)

visited = set()
for i in range(N):
    if i in not_loop:
        continue
    visited = bfs(i,visited)

print(len(visited))