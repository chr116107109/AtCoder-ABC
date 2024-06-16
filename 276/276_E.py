
H,W = map(int,input().split())
C = [input() for i in range(H)]
g = [[[] for j in range(W)] for i in range(H)]
for i in range(H):
    for j in range(W):
        if C[i][j] == 'S':
            S = (i,j)
        for x,y in [(i,j-1),(i-1,j),(i+1,j),(i,j+1)]:
            if 0<=x<H and 0<=y<W:
                if C[x][y] == '.':
                    g[i][j].append((x,y))

from collections import deque
def dfs(start,goal,g):
    q = deque()
    q.append(start)
    visited = set()
    while q:
        x,y = q.pop()
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for (s,t) in g[x][y]:
            q.append((s,t))
        
    #print(start,visited)
    for g in goal:
        if g in visited:
            return True
    else:
        return False



i,j = S
goal = set()
for x,y in [(i,j-1),(i-1,j),(i+1,j),(i,j+1)]:
    if 0<=x<H and 0<=y<W:
        if C[x][y] == '.':
            goal.add((x,y))

flag = 0
for x,y in goal:
    if dfs((x,y),goal-{(x,y)},g):
        flag = 1

if flag == 1:
    print('Yes')
else:
    print('No')