
def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N,K = map(int,input().split())
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


A = list(map(int,input().split()))
A.sort()

ans = 0

for i in range(N):
    if N-i-1 >= K-1:
        ans -= A[i]*cmb(N-i-1,K-1,mod)
        ans %= mod
        #print(ans)
for i in range(N):
    if i >= K-1:
        ans += A[i]*cmb(i,K-1,mod)
        ans %= mod
        #print(ans)


print(ans)