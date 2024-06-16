import sys
N,P = map(int,input().split())
mod = 998244353

d = [0] * (N)
p = P*pow(100,mod-2,mod)
q = (100-P)*pow(100,mod-2,mod)
if N == 1:
    print(1)
    sys.exit()
if N == 2:
    print((2*q+p)%mod)
    sys.exit()
d[0] = 1
d[1] = (2*q + p)%mod
for i in range(2,N):
    d[i] = (d[i-1]+1)*q + (d[i-2]+1)*p
    d[i] %= mod

print(d[-1])