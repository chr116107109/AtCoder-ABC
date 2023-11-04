import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math



N,M = map(int,input().split())

A = []
B = []
C = []
for i in range(N):
    T,X = map(int,input().split())

    if T == 0:
        A.append(X)
    if T == 1:
        B.append(X)
    if T == 2:
        C.append(X)

A.sort()
A.reverse()
B.sort()
#B.reverse()
C.sort()
C.reverse()


q = []
score = 0
for a in A:
    heappush(q,a)
    score += a
    if len(q) == M:
        break

ans = score

#print(ans,q)

for i in range(len(C)):
    n = C[i]
    heappush(q,10**18)

    #print(n,q,B)
    for i in range(n):
        if B == []:
            break
        b = B[-1]
        
        heappush(q,b)
        score += b
        B.pop()

    while len(q) > M:
        b = heappop(q)
        score -= b
        
    ans = max(score,ans)
    
print(ans)