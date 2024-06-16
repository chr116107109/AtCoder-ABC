
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M,K = map(int,input().split())

g = [set() for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].add(b-1)
    g[b-1].add(a-1)


ans = set()
police = {}
P = []
for i in range(K):
    p,h = map(int,input().split())
    police[p-1] = h
    P.append([p-1,h])


from collections import deque
def bfs(p,h,ans):
    q = deque()
    q.append((p,0,h))
    visited = {}
    while q:
        #print(q)
        s,d,e = q.popleft()
        ans.add(s+1)
        if s in visited:
            continue
        if s in police:
            e = max(police[s],e)

        visited[s] = d
        for t in g[s]:
            if e > 0:
                q.append((t,d+1,e-1))
    return visited

P.sort(key=lambda x:-x[1])
for p,h in P:
    if p+1 in ans:
        continue
    bfs(p,police[p],ans)

    #print(ans)


ans = list(ans)
ans.sort()
print(len(ans))
print(*ans)