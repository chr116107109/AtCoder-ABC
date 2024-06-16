import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

mod=998244353
d = [0] * (N+1)
d[-1] = 0
H = A[-1]*pow(N,mod-2,mod)

for i in range(N-1,-1,-1):
    d[i] += H  #pow(N,mod-2,mod)
    d[i] %= mod
    
    H += (d[i]+A[i-1])*pow(N,mod-2,mod)
    H %= mod
    #print(d[i],A[i-1],H)


print(d[0])