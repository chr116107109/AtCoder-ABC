

N,M,K = map(int,input().split())

A = list(map(int,input().split()))

g = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].append([b-1,i])
    g[b-1].append([a-1,i])

count = [0] * (N-1)

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t,i in g[s]:
            q.append((t,d+1))
    return visited

def get_path(s,t,visited):
    path = []
    now = t
    d = visited[t]
    while d > 0:
        d -= 1

        for x,i in g[now]:
            if visited[x] == d:
                now = x
                count[i] += 1
    

for i in range(M-1):
    visited = bfs(A[i]-1)
    if A[i+1]-1 in visited:
        get_path(A[i]-1,A[i+1]-1,visited)



d = [{} for i in range(N)] 
mod = 998244353
d[0][0] = 1

for i in range(N-1):

    for j in d[i]:
        if j+count[i] in d[i+1] and j+count[i] <= N*M:
            d[i+1][j+count[i]] += d[i][j]
            d[i+1][j+count[i]] %= mod
        else:
            d[i+1][j+count[i]] = d[i][j]
        if j-count[i] in d[i+1] and j-count[i] >= -N*M:
            d[i+1][j-count[i]] += d[i][j]
            d[i+1][j-count[i]] %= mod
        else:
            d[i+1][j-count[i]] = d[i][j]


if K in d[N-1]:
    print(d[N-1][K])
else:
    print(0)

