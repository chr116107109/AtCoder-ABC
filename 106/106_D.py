
N,M,Q = map(int,input().split())

d = [[] for i in range(N)]
for i in range(M):
    l,r = map(int,input().split())
    d[l-1].append(r-1)

A = [[0]*N for i in range(N)]
from heapq import heappush,heappop
for i in range(N):
    now = 0
    q = [0]*N
    for j in range(i,N):
        for k in d[j]:
            q[k] += 1
        now += q[j]
        A[i][j] = now
        
for i in range(Q):
    a,b = map(int,input().split())
    print(A[a-1][b-1])

