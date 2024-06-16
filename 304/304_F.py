
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
#N = 10**5
S = input()
#S = '#'*N
MM = int(N**(1/2))
fact = []
for i in range(1,MM+1):
    if N%i == 0:
        fact.append(i)
        fact.append(N//i)

fact.sort()
fact.pop()
M = len(fact)
d = [[True]*m for m in fact]

for i in range(N):

    for j,m in enumerate(fact):
        d[j][i%m] &= (S[i]=='#')

ans = 1
mod=998244353
p = {}
for i in range(len(d)):
    a = 1
    for boo in d[i]:
        if boo:
            a *= 2
            a %= mod
    
    m = fact[i]
    for j in fact:
        if j > m:
            break
        if m%j == 0 and j in p:
            a -= p[j]
            a %= mod

    p[fact[i]] = (a-1)%mod
    ans += a-1
    ans %= mod

print(ans)
    
