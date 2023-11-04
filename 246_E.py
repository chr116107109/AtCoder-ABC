

N = int(input())

start = list(map(int,input().split()))
goal = list(map(int,input().split()))
start = [start[0]-1, start[1]-1]
goal = [goal[0]-1, goal[1]-1]

S = [input() for i in range(N)]

inf = 10**10
visited = [[[inf,inf] for j in range(N)] for i in range(N)]

from collections import deque

q = deque()
q.append([start,0,1])
q.append([start,1,1])
while q:
    #print(q)
    s, dir, dist = q.popleft()
    
    if visited[s[0]][s[1]][dir] != inf:
        continue
    
    visited[s[0]][s[1]][dir] = dist
    if dir == 0:
        dif = 1
    else:
        dif = -1
    for t in [[s[0]-1,s[1]-dif],[s[0]+1,s[1]+dif]]:
        if not (0 <= t[0] < N) or not (0 <= t[1] < N) or S[t[0]][t[1]] == '#':
            continue
        #print(t)
        if visited[t[0]][t[1]][dir] == inf:
            q.appendleft([t,dir,dist])
    
    if s != start and visited[s[0]][s[1]][(dir+1)%2] == inf:
        q.append([s,(dir+1)%2, dist+1])

if visited[goal[0]][goal[1]][dir] == inf and visited[goal[0]][goal[1]][-dir] == inf:
    print(-1)
else:
    print(min(visited[goal[0]][goal[1]]))