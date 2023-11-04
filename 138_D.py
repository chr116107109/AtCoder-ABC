
N,Q = map(int,input().split())
g = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

d = [0] * N
for i in range(Q):
    p,x = map(int,input().split())
    d[p-1] += x

from collections import deque
q = deque()
q.append((0,0))
visited = [-1] * N

while q:
    #print(q)
    state, value = q.popleft()
    if visited[state] > -1:
        continue
    visited[state] = value + d[state]
    for next in g[state]:
        q.append((next,visited[state]))


print(*visited)