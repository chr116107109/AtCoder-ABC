import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
n = N


mod = 998244353

def f(n):
    i = 1

    X = N
    while i * 2 <= n:

        keta = len(str(N)) * i
        before = X  
        X *= pow(10,keta,mod)
        X %= mod
        X += before
        X %= mod
        i *= 2

#        print(X,i)

    n -= i
    #print(X,n,i)
    return X,n,i

X = 0
while True:
    Y,n,i = f(n)
    if X > 0:
        #print(X,Y,n)
        keta = len(str(N)) * i
        X *= pow(10,keta,mod)
        X %= mod
        X += Y
        X %= mod

    else:
        X = Y%mod
    if n == 0:
        break

print(X)