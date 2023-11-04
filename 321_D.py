import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M,P = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

B.sort()
C = [0]
for i in range(M):
    C.append(C[-1]+B[i])

ans = 0
for i in range(N):
    ind = bisect_left(B,max(0,P-A[i]))
    #print(ans,ind)
    ans += A[i]*ind + C[ind]
    ans += P*(M-ind)

print(ans)