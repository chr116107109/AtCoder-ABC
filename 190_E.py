import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

K = int(input())
C = list(map(int,input().split()))

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in g[s]:
            q.append((t,d+1))
    return visited

ans = K
V = []
for i in range(K):
    visited = bfs(C[i]-1)
    V.append(visited)


inf = 10**10
d = [[inf]*K for i in range(2**K)]
for i in range(K):
    d[2**i][i] = 1

for bit in range(1,2**K):

    for i in range(K):
        if bit&(1<<i) == 0:
            continue
        for j in range(K):
            if bit&(1<<j) != 0:
                continue

            #print(i,j)
            if not C[j]-1 in V[i]:
                continue
            d[bit|(1<<j)][j] = min(d[bit|(1<<j)][j], d[bit][i]+V[i][C[j]-1])
    #print(d)
    
if min(d[-1]) == inf:
    print(-1)
else:
    print(min(d[-1]))

