import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())

A = [-1]*N
# A[i]にはi行きの最終列車時刻が入る

g = [[] for i in range(N)]
for i in range(M):
    l,d,k,c,a,b = map(int,input().split())
    g[b-1].append(
        {
            "l":l,
            "d":d,
            "k":k,
            "c":c,
            "a":a - 1
        }
    )


q = []

INF=float('inf')
heappush(q,[-INF,N-1])
#-1,INF))
while q:
    #print(q)
    #v,T = q.popleft()
    T,v = heappop(q)
    #print(A)
    T = -T
    if A[v] >= 0 and T != INF:
        continue
    
    A[v] = T

    for e in g[v]:
        l,d,k,c,a = e["l"],e["d"],e["k"],e["c"],e["a"]
        if T - l - c < 0:
            continue
        if T == INF:
            #q.append([l + d*(k-1),a])
            heappush(q,[-(l + d*(k-1)),a])
        else:
            i = (T - l - c)//d
            i = min(i,k-1)
            heappush(q,[-(l + d*(i)),a])
            #q.append((a, l + d*i))

for a in A[:-1]:
    if a == -1:
        print("Unreachable")
    else:
        print(a)

