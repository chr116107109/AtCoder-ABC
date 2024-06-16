
S = input()
S = 's' * 5000
N = len(S)


mod = 998244353
from collections import Counter
import math

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

C = Counter()
for i in range(N):
    C[S[i]] += 1

d = [[0] * (N+1) for i in range(len(C)+1)]
d[0][0] = 1

for k,s in enumerate(C):
        
    for i in range(1,C[s]+1):
        for j in range(N+1):
            if i+j <= N:
                d[k+1][i+j] += 1#cmb(i+j,i,mod)*d[k][j]
                d[k+1][i+j] %= mod
            else:
                break

    for i in range(N+1):
        d[k+1][i] += d[k][i]
        d[k+1][i] %= mod
    
ans = 0
for i in range(1,N+1):
    ans += d[-1][i]
    ans %= mod

print(ans)