


N,M = map(int,input().split())
S = [input() for i in range(N)]
g = [[[],[]] for i in range(N)]
for i in range(N):
    for j in range(M):
        if S[i][j] == '1':
            g[i][0].append(i+j+1)
            g[i+j+1][1].append(i)

from collections import deque
def bfs(s,dir):
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in g[s][dir]:
            q.append((t,d+1))
    return visited

from_N = bfs(N-1,1)
from_0 = bfs(0,0)
A = []
for i in range(1,N-1):

    ans = 10**20
    for j in range(1,M+1):
        for k in range(1,M+1):
            if i-j < 0 or i+k > N-1 or j+k > M:
                continue

            if S[i-j][j+k-1] == '1' and i-j in from_0 and i+k in from_N:
                ans = min(ans, from_0[i-j] + from_N[i+k] + 1)
    
    if ans == 10**20:
        #print(-1)
        A.append(-1)
    else:
        #print(ans)
        A.append(ans)

print(*A)