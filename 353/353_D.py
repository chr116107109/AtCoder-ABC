import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = list(map(int,input().split()))

mod = 998244353

keta_sum = 0

for i in range(N):
    keta_sum += pow(10,len(str(A[i])),mod)
    keta_sum %= mod

ans = 0
_sum = sum(A)

for i in range(N):
    keta_sum -= pow(10,len(str(A[i])),mod)
    _sum -= A[i]

    ans += A[i]*keta_sum + _sum
    ans %= mod

    #print(keta_sum)
    #print(ans)

print(ans)