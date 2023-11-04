

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M,R = map(int,input().split())
A = list(map(int,input().split()))
g = [[] for i in range(N)]
inf = 10**20
d = [[inf]*N for i in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    g[a-1].append([b-1,c])
    g[b-1].append([a-1,c])
    d[a-1][b-1] = c
    d[b-1][a-1] = c


def WFM(d,N):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])                    

    return d

d = WFM(d,N)

ans = 10**20
for p in itertools.permutations(A):
    score = 0
    for i in range(len(p)-1):
        score += d[p[i]-1][p[i+1]-1]
    
    ans = min(score,ans)

print(ans)
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())
A = list(map(int,input().split()))

P = []
N = []
for i in range(N):
    if A[i] > 0:
        P.append(A[i])
    else:
        N.append(A[i])

if len(P) < K:
    pass
else:
    B = [1]
    for i in range(len(N)):
        B.append(B[-1]*N[i])

    C = [1]
    for i in range(len(P)):
