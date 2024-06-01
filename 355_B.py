import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = []
for i in range(N):
    C.append((A[i],'a'))
for i in range(M):
    C.append((B[i],'b'))

C.sort(key=lambda x:x[0])

for i in range(N+M-1):
    if C[i][1] == C[i+1][1] and C[i][1] == 'a':
        print("Yes")
        sys.exit()

print("No")