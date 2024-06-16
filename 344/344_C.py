import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())    
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))

d = set()

for i in range(N):
    for j in range(M):
        for k in range(L):
            d.add(A[i]+B[j]+C[k])

Q = int(input())

X = list(map(int,input().split()))  

for i in range(Q):
    if X[i] in d:
        print('Yes')
    else:
        print('No')