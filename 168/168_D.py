
N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)


from collections import deque
q = deque()
q.append((0,-1))
visited = set()

parent = [-1] * N
while q:
    s, par = q.popleft()
    if s in visited:
        continue
    visited.add(s)
    parent[s] = par+1
    for t in g[s]:
        q.append((t,s))

print('Yes')
for p in parent[1:]:
    print(p)
