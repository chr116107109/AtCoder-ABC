import itertools
import time

N,M = map(int,input().split())

def get_ab(M):
    lim = 400
    ab = []
    for a in range(lim+1):
        for b in range(lim+1):
            if a**2 + b**2 == M:
                ab.append([a,b])
    return ab

from collections import deque

ab = get_ab(M)
q = deque()
q.append([(1,1),0])
visited = [[-1]*N for i in range(N)]


while q:
    #print(q)
    [(i,j), d] = q.popleft()
    if visited[i-1][j-1] >= 0:
        visited[i-1][j-1] = min(visited[i-1][j-1],d)
        continue
    visited[i-1][j-1] = d
    #time.sleep(0.5)
    for [a,b] in ab:
        for [k,l] in [[i+a,j+b],[i+a,j-b],[i-a,j+b],[i-a,j-b]]:
            if 1<=k<=N and 1<=l<=N:
                q.append([(k,l),d+1])

for i in range(N):
    print(*visited[i])