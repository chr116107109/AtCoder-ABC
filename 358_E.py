import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return ((g1[n] * g2[r])%mod * g2[n-r]) % mod

mod = 998244353 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


K = int(input())
C = list(map(int,input().split()))
C.sort()
M = max(C)
d = [[0] * (M+1) for i in range(K+1)] 
d[0][0] = 1
sumd = [0] * (K+1)
sumd[0] = 1
for i in range(26):
    if C[i] == 0:
        continue
    dd = [[0] * (M+1) for i in range(K+1)] 
    dd[0][0] = 1

    for k in range(K,0,-1):
        dd[k][0] = sumd[k] % mod
        for j in range(1,C[i]+1):
            if k - j < 0:
                break
            dd[k][j] += sumd[k-j] * cmb(k,j,mod) % mod
            dd[k][j] %= mod  
            
        sumd[k] = sum(dd[k]) % mod

    d = dd[:]
    #print(*d, sep="\n")
    #print("")

ans = 0
for i in range(1,K+1):
    ans += sum(d[i])
    ans %= mod

print(ans)