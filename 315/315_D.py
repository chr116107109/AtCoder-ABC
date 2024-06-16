import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
g = [[set(),set()] for i in range(N)]
for i in range(N):
    A = list(map(int,input().split()))
    for a in A[1:]:
        g[i][0].add(a-1)
        g[a-1][1].add(i)

q = deque()
q.append(0)
ans = []

#print(g)
visited = {}
def dfs(s,visited):
    if s in visited:
        return
    if len(g[s][0]) == 0:
        ans.append(s+1)
        visited[s] = 1
        return 

    visited[s] = 1
    for t in g[s][0]:
        dfs(t,visited)

    ans.append(s+1)

dfs(0,{})

ans.pop()
print(*ans)