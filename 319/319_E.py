import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

def f(x,y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)

N,X,Y = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N-1)]

d = {}
period = 100
for i in range(period):

    now = i
    for j in range(N-1):
        p,t = A[j]
        if now%p == 0:
            now += t
        else:
            now += t + (p-now%p)
    
    d[tuple(i%A[j][0] for j in range(N-1))] = now - i

ans = []
Q = int(input())
for i in range(Q):
    q = int(input())

    
    start = tuple((q+X)%A[j][0] for j in range(N-1))
    ans.append(q+X+d[start]+Y)

print(*ans,sep='\n')