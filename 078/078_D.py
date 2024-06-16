
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,Z,W = map(int,input().split())
A = list(map(int,input().split()))

INF=float('inf')

from functools import cache,lru_cache
@cache
def solve(X,i,bit):
    print(X,i,bit,'s')
    if i == N-1:
        if bit == 0:
            return A[i],X
        else:
            return X,A[i]

    if bit == 0:
        score = -1
    else:
        score = INF
    
    if bit == 0:
        x,y = 0,X
    else:
        x,y = X,0
    for j in range(i,N-1):
        if bit == 0:
            a,b = solve(A[j],j+1,(bit+1)%2)
            print(a,b)
            if abs(a-b) > score:
                x,y = a,b
                score = abs(a-b)

        else:
            a,b = solve(A[j],j+1,(bit+1)%2)
            if abs(a-b) < score:
                x,y = a,b
                score = abs(a-b)

    print(x,y,'g')
    return x,y


x,y = solve(W,0,0)
print(abs(x-y))