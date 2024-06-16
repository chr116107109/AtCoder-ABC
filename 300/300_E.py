
N = int(input())

A = {2:0,3:0,5:0}
for i in [2,3,5]:
    while N%i == 0:
        N //= i
        A[i] += 1

import sys
if N!=1:
    print(0)
    sys.exit()
d = [[[0 for i in range(A[5]+1)] for j in range(A[3]+1)] for k in range(A[2]+1)]

d[0][0][0] = 1

mod = 998244353
inv = pow(5,mod-2,mod)

for k in range(A[5]+1):
    for j in range(A[3]+1):
        for i in range(A[2]+1):
            
            if i + 1 <= A[2]:
                d[i+1][j][k] += d[i][j][k]*inv
                d[i+1][j][k] %= mod
            if j + 1 <= A[3]:
                d[i][j+1][k] += d[i][j][k]*inv
                d[i][j+1][k] %= mod
            if i + 2 <= A[2]:
                d[i+2][j][k] += d[i][j][k]*inv
                d[i+2][j][k] %= mod
            if k + 1 <= A[5]:
                d[i][j][k+1] += d[i][j][k]*inv
                d[i][j][k+1] %= mod
            if i + 1 <= A[2] and j+1 <= A[3]:
                d[i+1][j+1][k] += d[i][j][k]*inv
                d[i+1][j+1][k] %= mod

print(d[A[2]][A[3]][A[5]])