import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

S = [input() for i in range(N)]

        
from collections import deque
def bfs(s):
    q = deque()
    q.append(s)
    ans = set()
    visited = [[0]*M for i in range(N)]
    while q:
        #print(q)
        s = q.popleft()
        i,j = s
        if visited[i][j] != 0:
            continue
        visited[i][j] = 1

        now = [i,j]
        while now[0] < N and S[now[0]][now[1]] == '.':
            ans.add(now[0]*M+now[1])
            now[0] += 1
    
        now[0] -= 1
        q.append(now)
        now = [i,j]
        while now[0] >= 0 and S[now[0]][now[1]] == '.':
            ans.add(now[0]*M+now[1])
            now[0] -= 1
            
        now[0] += 1
        q.append(now)
        
        now = [i,j]
        while now[1] < M and S[now[0]][now[1]] == '.':
            ans.add(now[0]*M+now[1])
            now[1] += 1
            
        now[1] -= 1
    
        q.append(now)
        
        now = [i,j]
        while now[1] >= 0 and S[now[0]][now[1]] == '.':
            ans.add(now[0]*M+now[1])
            now[1] -= 1
            
        now[1] += 1
    
        q.append(now)
        
        #print(visited)
    return visited,ans


_,ans = bfs([1,1])

print(len(ans))