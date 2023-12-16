import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]

ok = True

ans  = 0
target = -1
for j,b in enumerate(B):
    if Counter(A[0]) == Counter(B[j]):
        target = j
if target == -1:
    ok = False   


if not ok:
    print(-1)
    sys.exit()

a = A[0][:]
b = B[target][:]

#print(a,b)

for i in range(W):
    for j in range(i,W):
        if b[i] == a[j]:
            ans += j - i
            for k in range(j,i,-1):
                a[k-1],a[k] = a[k],a[k-1]
                for l in range(H):
                    A[l][k-1],A[l][k] = A[l][k],A[l][k-1]
                
                #print(a,i,j)
            break

    #print(a)



a = [A[i][0] for i in range(W)]
b = [B[i][target] for i in range(W)]

#print(a,b)

for i in range(H):
    for j in range(i,H):
        if B[i] == A[j]:
            ans += j - i
            for k in range(j,i,-1):
                a[k-1],a[k] = a[k],a[k-1]
                A[k-1],A[k] = A[k],A[k-1]
            break


if A == B:
    print(ans)
else:
    print(-1)