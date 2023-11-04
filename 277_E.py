
N,M,K = map(int,input().split())
g0 = [[] for i in range(N)]
g1 = [[] for i in range(N)]
for i in range(M):
    u,v,a = map(int,input().split())
    if a == 0:
        g0[u-1].append(v-1)
        g0[v-1].append(u-1)
    if a == 1:
        g1[u-1].append(v-1)
        g1[v-1].append(u-1)
S = set(map(int,input().split()))

from collections import deque
q = deque()
q.append((0,1,0)) #vartex, stateOfSwitch, distance
visited = {}

while q:
    s,a,d = q.popleft()
    if (s,a) in visited:
        continue
    visited[(s,a)] = d
    if s == N-1:
        break
    if s+1 in S:
        for t in g0[s]:
            q.append((t,0,d+1))
        for t in g1[s]:
            q.append((t,1,d+1))
    else:
        if a == 0:
            for t in g0[s]:
                q.append((t,a,d+1))
        if a == 1:
            for t in g1[s]:
                q.append((t,a,d+1))
        
ans = -1 
if (N-1, 0) in visited:
    ans = visited[(N-1,0)]

if (N-1, 1) in visited:
    ans = visited[(N-1,1)]

print(ans)