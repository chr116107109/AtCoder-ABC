
N = int(input())
from collections import deque
g = [[] for i in range(N)]
for i in range(N-1):
    A,B = map(int,input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)
for i in range(N):
    g[i].sort(key = lambda x:-x)

q = []
q.append(0)
visited = set()
parent = [-1] * N
path = []
while q:
    #print(q)
    s = q.pop()    
    visited.add(s)
    path.append(s+1)
    #print(s,g)
    if s == 0 and g[s] == []:
        break
    while g[s]:
        t = g[s].pop()
        if not t in visited:
            parent[t] = s
            q.append(t)
            break
    if q == []:
        q.append(parent[s])

print(*path)