import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,K = map(int,input().split())

A = [-1] * N
q = ['?'] + list(range(1,K+1))
print(*q)
res1 = int(input())
q = ['?'] + list(range(2,K+2))
print(*q)
res2 = int(input())
A[0] = 1
if res1 == res2:
    A[K] = 1
else:
    A[K] = 0

num = list(range(1,N+2))
for i in range(K-1):
    q = ['?'] + num[0:i+1] + num[i+2:K+1]
    print(*q)
    res3 = int(input())
    
    if res2 != res3:
        A[i+1] = 0
    else:
        A[i+1] = 1

for i in range(K+1,N):
    q = ['?'] + num[1:K] + [i+1]
    print(*q)
    res3 = int(input())
    
    if res1 != res3:
        A[i] = 0
    else:
        A[i] = 1


x = sum(A[:K])%2
if x != res1:
    for i in range(N):
        A[i] += 1
        A[i] %= 2

A = ['!'] + A
print(*A)
