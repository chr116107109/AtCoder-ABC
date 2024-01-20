import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W = map(int,input().split())
S = [input() for _ in range(H)]
S = " ".join(S)  

def convert(s,type):
    ori = []
    res = []
    t = s.split()
    #print(t)
    for i in range(H):
        res.append([])
        ori.append([])
        for j in range(W):
            ori[i].append(t[i*W+j])
            res[i].append(t[i*W+j])
    if type == 1:
        for i in range(H-1):
            for j in range(W-1):
                res[i][j] = ori[H-1-i - 1][W-1-j - 1]
    elif type == 2:
        for i in range(H-1):
            for j in range(W-1):
                res[i+1][j] = ori[H-1-i - 1 + 1][W-1-j - 1]
    elif type == 3:
        for i in range(H-1):
            for j in range(W-1):
                res[i][j+1] = ori[H-1-i - 1][W-1-j - 1 + 1]
    elif type == 4:
        for i in range(H-1):
            for j in range(W-1):
                res[i+1][j+1] = ori[H-1-i - 1 + 1][W-1-j - 1 + 1]
    
    return " ".join([" ".join(res[i]) for i in range(H)])

from collections import deque
def bfs(s,max_depth):
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        
        visited[s] = d

        if d >= max_depth:
            continue

        for type in [1,2,3,4]:
            q.append((convert(s,type),d+1))
    return visited

visited_left = bfs(S,10)
result = " ".join([str(i) for i in range(1,H*W+1)])
visited_right = bfs(result,10)

ans = 10**20

for key in visited_left:
    if key in visited_right:
        ans = min(ans,visited_left[key] + visited_right[key])

if ans == 10**20:
    print(-1)
else:
    print(ans)
