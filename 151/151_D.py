

H,W = map(int,input().split())
S = [input() for i in range(H)]
from collections import deque
def bfs(s):
    q = deque()
    q.append([s,0])
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in [(s[0],s[1]-1),(s[0],s[1]+1),(s[0]+1,s[1]),(s[0]-1,s[1])]:
            if not (0<=t[0]<H and 0<=t[1]<W):
                continue
            if S[t[0]][t[1]] == '.':
                q.append([t,d+1])

    return max(visited.values())

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            ans = max(ans,bfs((i,j)))

print(ans)