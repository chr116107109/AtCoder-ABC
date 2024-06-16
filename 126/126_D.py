
N = int(input())

g = [[] for i in range(N)]
for i in range(N-1):
    a,b,c = map(int,input().split())
    g[a-1].append([b-1,c])
    g[b-1].append([a-1,c])

from collections import deque

q = deque()
q.append((0,0))
color = [-1] * N

while q:
    s,c = q.popleft()
    if color[s] != -1:
        continue
    if c%2 == 1:
        color[s] = 1
    else:
        color[s] = 0
    
    for t,dif in g[s]:
        q.append((t,c+dif))

for i in range(N):
    print(color[i])