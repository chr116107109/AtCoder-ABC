
from heapq import heappush,heappop
from collections import deque

N,M,K = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    A,B,C = map(int,input().split())
    g[A-1].append([B-1,C,i+1]) #[to, cost, id]

E = list(map(int,input().split()))
invE = [[] for i in range(M+1)]
for i in range(K):
    invE[E[i]].append(i+1)

inf = 10**30
dist = [inf] * N
dist[0] = 0

q = []
heappush(q,(0,0,0))

while q:
    #print(q)
    d, s, prev_ind = heappop(q)
    for t,cost,ind in g[s]:
        if d + cost < dist[t]:
            for next_ind in invE[ind]:
                if next_ind > prev_ind:
                    dist[t] = d + cost
                    heappush(q,(dist[t], t, next_ind))


if dist[-1] == inf:
    print(-1)
else:
    print(dist[-1])