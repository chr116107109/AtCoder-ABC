

H,W = map(int,input().split())

S = [input() for i in range(H)]

from collections import deque
q = deque()
q.append([(0,0),0])

visited = [[-1]*W for i in range(H)]
while q:
    s, d = q.popleft()
    if visited[s[0]][s[1]] > -1:
        continue
    visited[s[0]][s[1]] = d

    for t in [(s[0]+1,s[1]), (s[0]-1,s[1]), (s[0],s[1]+1), (s[0],s[1]-1)]:
        if not 0<=t[0]<H or not 0<=t[1]<W:
            continue

        if S[t[0]][t[1]] == '.':
            q.appendleft([t,d])
        if S[t[0]][t[1]] == '#':
            for u in [(t[0],t[1]), (t[0]+1,t[1]), (t[0]-1,t[1]), (t[0],t[1]+1), (t[0],t[1]-1), (t[0]+1,t[1]+1), (t[0]+1,t[1]-1), (t[0]+1,t[1]-1), (t[0]-1,t[1]+1)]:
                if not 0<=u[0]<H or not 0<=u[1]<W:
                    continue
                if visited[u[0]][u[1]] == -1:
                    q.append([u,d+1])

print(visited[H-1][W-1])