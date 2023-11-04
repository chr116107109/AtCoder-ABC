
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

C = []
P = []
R = []
for i in range(N):
    p = list(map(int,input().split()))
    C.append(p[0])
    P.append(p[1])
    R.append(p[2:])

d = [0] * (M+1)

for i in range(M-1,-1,-1):
    exp = 10**20
    for j in range(N):
        score = 0
        if not 0 in R[j]:
            for k in range(P[j]):
                if R[j][k] != 0:
                    score += (d[min(i+R[j][k],M)]) / P[j]
            score += C[j]
        else:
            a = 0
            n_zero = 0
            for k in range(P[j]):
                if R[j][k] == 0:
                    n_zero += 1
            for k in range(P[j]):
                if R[j][k] != 0:
                    a += (d[min(i+R[j][k],M)])/(P[j]-n_zero)
    
            score = C[j]*P[j]/(P[j]-n_zero) + a

        exp = min(exp,score)

    
    d[i] = exp
    #print(d)

print(d[0])