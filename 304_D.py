import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


W,H = map(int,input().split())
N = int(input())

P = [list(map(int,input().split())) for i in range(N)]

P.sort(key=lambda x:x[0])

NA = int(input())
A = list(map(int,input().split()))
A.append(10**10)
NB = int(input())
B = list(map(int,input().split()))
B.append(10**10)

i = 0
j = 0

d = [[] for i in range(NA+1)]

nmax = 0
nmin = 10**10
while i < NA+1:
    count = Counter()
    while j < N and P[j][0] < A[i]:
        #d[i].append(P[j][1])
        k = bisect_left(B,P[j][1])
        count[k] += 1
        j += 1

    a = 0
    b = 10**10
    if len(count) > 0:
        a = max(count.values())
        b = min(count.values())
    
    if len(count) < NB+1:
        b = 0
    nmin = min(nmin,b)
    nmax = max(nmax,a)
    i += 1

    
print(nmin,nmax)

