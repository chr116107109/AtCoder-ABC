
H,W,T = map(int,input().split())

A = [input() for i in range(H)]

p = []
for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            S = [i,j]
        if A[i][j] == 'G':
            G = [i,j]
        if A[i][j] == 'o':
            p.append([i,j])

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
        
        for t in [(s[0]+1,s[1]),(s[0]-1,s[1]),(s[0],s[1]+1),(s[0],s[1]-1)]:
            if 0<=t[0]<H and 0<=t[1]<W and A[t[0]][t[1]] != '#':
                q.append((t,d+1))

    return visited

inf = 10**20
V = [[inf]*len(p) for i in range(len(p))]
vs = [0] * len(p)
visited = bfs(tuple(S))
import sys
if not tuple(G) in visited or visited[tuple(G)] > T:
    print(-1)
    sys.exit()
    
for j,t in enumerate(p):
    if tuple(t) in visited:
        vs[j] = visited[tuple(t)]


vg = [0] * len(p)
visited = bfs(tuple(G))
for j,t in enumerate(p):
    if tuple(t) in visited:
        vg[j] = visited[tuple(t)]

for i,s in enumerate(p):
    visited = bfs(tuple(s))
    for j,t in enumerate(p):
        if tuple(t) in visited:
            V[i][j] = visited[tuple(t)]

d = [[inf] * len(p) for i in range(2**len(p))]

for i in range(len(p)):
    d[2**i][i] = vs[i]
    d[0][i] = 0

ans = 0
for i in range(2**len(p)):
    count = 0
    for j in range(len(p)):
        if i&(1<<j) != 0:
            count += 1

    for j in range(len(p)):
    
        if i&(1<<j) == 0:
            continue
        if d[i][j]+vg[j] <= T:
            ans = max(ans,count)

        for k in range(len(p)):
            if i&(1<<k) == 0:
                d[i|(1<<k)][k] = min(d[i|(1<<k)][k], d[i][j]+V[j][k])
            
        


print(ans)
