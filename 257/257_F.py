
import collections
from dis import dis
from hashlib import new


N,M = map(int,input().split())
g = [[] for i in range(N)]

pend = []
for i in range(M):
    u,v = map(int,input().split())
    if u == 0:
        pend.append(v-1)
    else:
        g[u-1].append(v-1)
        g[v-1].append(u-1)

import heapq
def dikstra(start,g, visited):
    q = [(0,start)]
    while q:
        dist,s = heapq.heappop(q)
        if s in visited:
            continue
        visited[s] = dist
        for t in g[s]:
            if t in visited:
                if visited[t] > dist + 1:
                    heapq.heappush(q,(dist+1,t))
            else:
                heapq.heappush(q,(dist+1,t))
    return visited


visited = {}
dist = dikstra(0,g,visited)

ans = []
for i in range(N):
    muda = []
    for p in pend:
        if i != p:
            if not p in g[i]:
                g[i].append(p)
                muda.append([i,p])
            if not i in g[p]:
                g[p].append(i)
                muda.append([p,i])
    
    print(g)
    
    if (not i in dist) and (not i in g[0]):
        if N-1 in dist:
            ans.append(dist[N-1])
        else:
            ans.append(-1)
    else:
        new_dist = dikstra(i,g,dist)
        if N-1 in new_dist and N-1 in dist:
            ans.append(min(new_dist[N-1],dist[N-1]))
        elif (N-1 in new_dist) and (not N-1 in dist):
            ans.append(new_dist[N-1])
        elif (not N-1 in new_dist) and (N-1 in dist):
            ans.append(dist[N-1])
        elif (not N-1 in new_dist) and (not N-1 in dist):
            ans.append(-1)

    for [s,t] in muda:
        g[s].remove(t)

print(ans)

