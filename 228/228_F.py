

N,K,M = map(int,input().split())
mod = 998244353

if M%mod == 0:
    print(0)
else:
    x = pow(K,N,mod-1)
    ans = pow(M,x,mod)
    print(ans)