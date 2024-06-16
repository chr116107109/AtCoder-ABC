

H,W,K = map(int,input().split())
a,b,c,d = map(int,input().split())
mod = 998244353 
start = [a-1,b-1]
goal = [c-1,d-1]
dh = [[0,0] for i in range(K+1)]
dw = [[0,0] for i in range(K+1)]
if goal[0] == start[0]:
    dh[0][1] = 1
else:
    dh[0][0] = 1
if goal[1] == start[1]:
    dw[0][1] = 1
else:
    dw[0][0] = 1

for i in range(1,K+1):
    dh[i][0] = dh[i-1][1]*(H-1) + dh[i-1][0]*(H-2)
    dh[i][0] %= mod
    dh[i][1] = dh[i-1][0]
    dh[i][1] %= mod

    dw[i][0] = dw[i-1][1]*(W-1) + dw[i-1][0]*(W-2)
    dw[i][0] %= mod
    dw[i][1] = dw[i-1][0]
    dw[i][1] %= mod

ans = 0


def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

N = K
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

for i in range(K+1):
    ans += dh[i][1]*dw[K-i][1]*cmb(K,i,mod)
    ans %= mod

print(ans)