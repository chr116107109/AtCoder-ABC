
N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    g[a-1].append([b-1,c])

from heapq import heappush,heappop 

def djkstra(start):
    q = []
    for t,d in g[start]:
        heappush(q,[d,t])
    visited = set()
    while q:
        #print(q)
        d, s = heappop(q)
        if s == start:
            return d
        if s in visited:
            continue
        visited.add(s)
        for t,c in g[s]:
            heappush(q,[d+c,t])

    return -1

for i in range(N):
    print(djkstra(i))