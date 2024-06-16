import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,K,P = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

inf = 10**20
M = (P+1)**K
d = [inf] * ((P+1)**K)
after = [inf] * ((P+1)**K)
d[0] = 0

for i in range(N):
    
    C = A[i][0]
    B = A[i][1:]

    for bit in range(M):
        if d[bit] == inf:
            continue
        after[bit] = min(after[bit],d[bit])
        score = [0] * K
        sixbit = bit
        for j in range(K-1,-1,-1):
            s = sixbit//pow(P+1,j)
            score[j] = s
            sixbit %= pow(P+1,j)
        #print(score)
        nextscore = [0] * K
        for j in range(K):
            nextscore[j] = min(P,score[j]+B[j])
        #print(nextscore)
        nextbit = 0
        for j in range(K):
            nextbit += nextscore[j]*pow(P+1,j)
        after[nextbit] = min(d[bit] + C, after[nextbit])
        #print(nextbit,bit,d[bit],after[nextbit])


    d = after[:]

if d[-1] == inf:
    print(-1)
else:
    print(d[-1])