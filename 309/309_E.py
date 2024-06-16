import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
P = list(map(int,input().split()))
g = [[] for i in range(N)]
for i in range(N-1):
    a,b = i+1,P[i]-1
    g[a].append(b)
    g[b].append(a)

d = {}
for i in range(M):
    x,y = map(int,input().split())
    if x-1 in d:
        d[x-1] = max(d[x-1],y)
    else:
        d[x-1] = y

q = deque()
if 0 in d:
    q.append([0,d[0]+1])
else:
    q.append([0,0])

visited = {}
ans = set()

while q:
    #print(q)
    s,x = q.popleft()
    

    if s in visited:
        continue
    visited[s] = x
    if s in d:
        x = max(x,d[s]+1)
    if x > 0:
        ans.add(s)

    for t in g[s]:
        if x > 0:
            q.append([t,x-1])
        else:
            q.append([t,0])

print(len(ans))