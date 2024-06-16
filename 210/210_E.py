

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(M)]

A.sort(key=lambda x:x[1])

L = N
ans = 0
for i in range(M):
    #print(ans)
    if math.gcd(L,A[i][0]) == 1:
        ans += (L-1)*A[i][1]
        L = 1
        break
    elif A[i][0]%L == 0:
        continue
    else:
        ans += (L//math.gcd(L,A[i][0])-1) * math.gcd(L,A[i][0]) * A[i][1]
        L = math.gcd(L,A[i][0])
    if L == 1:
        break

if L != 1:
    print(-1)
else:
    print(ans)
