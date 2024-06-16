
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

from collections import deque
def bfs(start,g,k):
    q = deque()
    q.append((start,0))
    #dist = [-1] * len(g)
    #dist[start] = 0
    visited = set()
    lesk = 0
    while q:
        s,depth = q.popleft()
        if s in visited:
            continue
        if depth <= k:
            lesk += s+1
        visited.add(s)
        #print(q,s)
        #print(lesk)
        for t in g[s]:
            if depth < k:
                #dist[t] = dist[s] + 1
                #lesk += s+1
                #if depth < k - 1:
                q.append((t,depth+1))
        #print(q)
        #print(lesk)
    return lesk,visited

Q = int(input())

for i in range(Q):
    start, k = map(int,input().split())
    lesk,visited = bfs(start-1,g,k)
    #print(visited)
    print(lesk)