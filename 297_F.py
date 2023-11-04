
H,W,K = map(int,input().split())

A = [0] * (H+1)
B = [0] * (W+1)

mod = 998244353 

import math
if K >= H:
    com = pow(H,K)
else:
    com = math.perm(H)//math.perm(K)//math.perm(H-K)
inv = pow(com, mod-2, mod)
for i in range(H+1):
    A[i] = pow(i,max(K-2,0),mod) * (H-i) * inv
    A[i] %= mod

if K >= H:
    com = pow(W,K)
else:
    com = math.perm(W)//math.perm(K)//math.perm(W-K)
inv = pow(com, mod-2, mod)

for i in range(H+1):
    B[i] = pow(i,max(K-2,0),mod) * (W-i) * inv
    B[i] %= mod

ans = 0
for i in range(H+1):
    for j in range(W+1):
        ans += (i+1)*(j+1) * A[i]*B[j]
        ans %= mod

print(ans)