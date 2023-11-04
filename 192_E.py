

N,M,X,Y = map(int,input().split())
X -= 1
Y -= 1
g = [[] for i in range(N)]
for i in range(M):
    a,b,c,d = map(int,input().split())
    g[a-1].append([b-1,c,d])
    g[b-1].append([a-1,c,d])

from heapq import heappush,heappop
q = []
heappush(q,[0,X])
visited = {}

while q:
    now, s = heappop(q)
    if s in visited:
        continue
    visited[s] = now

    for t, d, k in g[s]:
        next = now + -now%k + d
        heappush(q,[next,t])


if Y in visited:
    print(visited[Y])
else:
    print(-1)