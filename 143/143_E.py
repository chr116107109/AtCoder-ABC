N,M,L = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    g[a-1].append([b-1,c])
    g[b-1].append([a-1,c])

from collections import deque
def bfs(s):
    q = deque()
    q.append([s,0])
    inf = 10**10
    visited = [inf] * N
    ene = [[0]*N for i in range(N+1)]
    ene[0][s] = L
    while q:
        s,d = q.popleft()
        if visited[s] < inf:
            continue
        visited[s] = d
        e = ene[d][s]
        for t,cost in g[s]:
            if cost > L:
                continue
            if cost > e:
                q.append([t,d+1])
                ene[d+1][t] = max(ene[d+1][t],L-cost)
            else:
                q.appendleft([t,d])
                ene[d][t] = max(ene[d][t],e-cost)
    return visited

dist = []
for i in range(N):
    dist.append(bfs(i))

Q = int(input())

ans = []
for i in range(Q):
    s,t = map(int,input().split())
    s -= 1
    t -= 1

    if dist[s][t] < 10**10:
        ans.append(dist[s][t])
    else:   
        ans.append(-1)

print(*ans, sep='\n')