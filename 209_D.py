
from collections import deque


N,Q = map(int,input().split())
g = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

A = set()

q = deque()
q.append((0,0))
visited = {}
while q:
    s,d = q.popleft()
    if s in visited:
        continue
    visited[s] = d
    if d%2 == 0:
        A.add(s+1)
    for t in g[s]:
        q.append((t,d+1))

for i in range(Q):
    c,d = map(int,input().split())
    if (c in A and d in A) or (not c in A and not d in A):
        print('Town')
    else:
        print('Road')