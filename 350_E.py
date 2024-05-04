import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,A,X,Y = map(int,input().split())

from collections import deque
def bfs():
    q = []
    q.append(1)
    visited = {}
    visited[1] = 1/6 * Y
    Value = {}
    while q:
        #print(Value)
        s = heappop(q)
        if s > N:
            continue

        if Value.get(s,0) > 0:
            continue
        value = visited[s]
        Value[s] = min((value+X)/(1-1/6), X+Value.get(s//A,0))
        for i in range(2,7):
            if s*i in visited:
                visited[s*i] += (Y+Value[s])/6
            else:   
                visited[s*i] = (Y+Value[s])/6
            heappush(q,s*i)


    return Value

        
V = bfs()

if N in V:
    print(V[N])
else:
    
    q = []
    heappush(q,(-N,1))
    visited = {}
    while q:
        print(q[0])
        s,d = heappop(q)
        s = -s
        if s in visited:
            visited[s] = min(visited[s],d)  
            continue
        visited[s] = d
        if s in V:
            continue
        q.append((-(s//A),d+X))
        for i in range(2,7):
            q.append((-(s//i),d+Y/6))

    ans = 10**50

    for k in visited:
        if k in V:
            print(k,V[k],visited[k], V[k]+visited[k])
            ans = min(ans,V[k]+visited[k])

    print(ans)