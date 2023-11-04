import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]

A.sort(key=lambda x:x[0])

now = 0
for i in range(N):
    now += A[i][1]

if now <= K:
    print(1)
    sys.exit()
day = 0

for i in range(N):

    if A[i][0]<=day:
        now -= A[i][1]
    else:
        now -= A[i][1]
        day = A[i][0]

    if now <= K:
        break

print(day+1)
#if day == 1 and K != 0:
#    print(1)
#else:
#    print(day+1)