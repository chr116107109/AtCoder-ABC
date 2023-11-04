import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
from sys import stdin

N,A,B,C = map(int,input().split())

D = [list(map(int, stdin.readline().split())) for _ in range(N)]

from collections import deque
INF=10**20
from heapq import heappush,heappop
def djkstra_A(s):
    q = []
    M = 10**10
    heappush(q,s)
    visited = [INF]*N
    while q:
        d= heappop(q)
        d,s = d//M,d%M
        if visited[s] < INF:
            continue
        visited[s] = d
        for t in range(N):
            if s == t:
                continue

            w =  D[min(s,t)][max(s,t)-min(s,t)]*A
            if visited[t] < INF:
                continue
            
            heappush(q,M*(d+w)+t)
        if visited[N-1] < INF:
            break
    return visited
    
def djkstra_B(s):
    q = []
    M = 10**10
    heappush(q,s)
    visited = [INF]*N
    while q:
        d= heappop(q)
        d,s = d//M,d%M
        
        if visited[s] < INF:
            continue
        visited[s] = d
        for t in range(N):
            if s == t:
                continue
            w = D[min(s,t)][max(s,t)-min(s,t)]*B+C
            if visited[t] < INF:
                continue
            heappush(q,M*(d+w)+t)
        if visited[0] < INF:
            break
    return visited
    
car = djkstra_A(0)
train = djkstra_B(N-1)

ans = min(car[N-1],train[0])
for i in range(N):
    ans = min(ans,car[i]+train[i])

print(ans)