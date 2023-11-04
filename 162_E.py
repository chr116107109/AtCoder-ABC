

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,K = map(int,input().split())

ans = 0
mod = 10**9 + 7
count = 0
for i in range(K,0,-1):
    ans += max((pow(K//i, N, mod) - count),1)%mod * i
    ans %= mod
    count += pow(K//i, N, mod)
    count %= mod

    print(ans,count)

def greed(N,K):
    ans = 0
    g2p = Counter()
    for p in itertools.product(range(1,K+1),repeat=N):
        g = 0
        for i in range(N):
            g = math.gcd(g,p[i]) 
        ans += g
        g2p[g] += 1
    return ans,g2p

print(greed(N,K))