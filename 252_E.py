
N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    A,B,C = map(int,input().split())
    g[A-1].append([B-1,C,i+1])
    g[B-1].append([A-1,C,i+1])

from heapq import heappush,heappop
q = []
heappush(q,(0,(0,-1)))
ans = []
visited = set()
while q:
    d,(s,a) = heappop(q)
    if s in visited:
        continue
    visited.add(s)
    ans.append(a)
    for t,c,num in g[s]:
        heappush(q,(d+c,(t,num)))

print(*ans[1:])