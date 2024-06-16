

N,M = map(int,input().split())

g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

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
        for t in g[s]:
            q.append((t,d+1))
    return visited

K = int(input())
white = set()
black = []
for i in range(K):
    p,d = map(int,input().split())
    visited = bfs(p-1)
    black.append(set())
    for j in range(N):
        if j in visited and visited[j] == d:
            black[-1].add(j)
        if j in visited and visited[j] < d:
            white.add(j)

import sys
ans = ['0']*N
for b in black:
    for w in white:
        if w in b:
            b.remove(w)
    if len(b) == 0:
        print('No')
        sys.exit()
    
    for i in b:
        ans[i] = '1'
        break

print('Yes')
if black == []:
    print('1'*N)
else:   
    print(''.join(ans))

