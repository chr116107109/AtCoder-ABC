
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
g = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)


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

def get_path(a,b,visited):
    now = b
    path = [b]
    while now != a:
        for c in g[now]:
            if visited[c] == visited[now]-1:
                now = c
                path.append(now)

    path.reverse()
    return path

visited = bfs(0)
path = get_path(0,N-1,visited)

m = visited[N-1]//2

g[path[m]].remove(path[m+1])
g[path[m+1]].remove(path[m])


b = bfs(0)
w = bfs(N-1)

if len(b) > len(w):
    print('Fennec')
else:
    print('Snuke')