
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right

N,M = map(int,input().split())

S = []
g = [[] for i in range(N+M)]

for i in range(N):
    _ = input()
    A = list(map(int,input().split()))

    for a in A:
        g[i].append(N+a-1)
        g[N+a-1].append(i)
    
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

visited = bfs(N)

if N+M-1 in visited:
    print((visited[N+M-1]-2)//2)
else:
    print(-1)