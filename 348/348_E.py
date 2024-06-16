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

C = list(map(int,input().split()))
visited = {}
ot = []
inout = [[0,0] for i in range(N)]
parent = [-1]*N
 
def dfs(s,d):
    if len(g[s]) == 1 and s != 0:
        visited[s] = d
        inout[s][0] = len(ot)
        ot.append(s)
        inout[s][1] = len(ot)
        ot.append(s)
        return
    
    visited[s] = d
    inout[s][0] = len(ot)
    ot.append(s)
    for t in g[s]:
        if t in visited:
            continue
        parent[t] = s
        dfs(t,d+1)
    inout[s][1] = len(ot)
    ot.append(s)

    return


dfs(0,0)

len_childs = [0]*N  
for i in range(N):
    len_childs[i] = (inout[i][1] - inout[i][0] - 1) // 2

sum_C = sum(C)

sum_Cd = 0
for i in range(N):
    sum_Cd += C[i] * visited[i]

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0,0))
    v = {}
    inf = 10**20
    ans = inf
    while q:
        s,d,z = q.popleft()
        if s in v:
            continue
        v[s] = d

        childs = len_childs[s] + 1
        score = visited[s] * sum_C + sum_Cd - 2 * (C[s] * childs * d + z)
        ans = min(ans,score)
        print(s,d,z,score)  

        for t in g[s]:
            x = (childs - len_childs[t] + 1) * (d) * C[s]
            q.append((t,d+1,z + x))

    return ans


print(bfs(0))