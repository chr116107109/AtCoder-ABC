

N,M = map(int,input().split())
A = list(map(int,input().split()))
g = [[set(),0] for i in range(N)]
for i in range(M):
    U,V = map(int,input().split())
    g[U-1][0].add(V-1)
    g[V-1][0].add(U-1)

q = []
from heapq import heappush,heappop
for i in range(N):
    cost = 0
    for j in g[i][0]:
        cost += A[j]
    g[i][1] = cost
    heappush(q,[cost,i])

is_deleted = set()
ans = 0
while q:
    #print(q)
    cost,s = heappop(q)
    if s in is_deleted:
        continue
    is_deleted.add(s)
    ans = max(ans,cost)
    for t in g[s][0]:
        if t in is_deleted:
            continue
        g[t][0].remove(s)
        g[t][1] -= A[s]
        heappush(q,[g[t][1],t])

print(ans)