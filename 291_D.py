

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

d = [[0] * 2 for i in range(N)]

d[0][0] = 1
d[0][1] = 1

mod = 998244353

for i in range(1,N):

    if A[i-1][0] != A[i][0]:
        d[i][0] += d[i-1][0]
    if A[i-1][1] != A[i][0]:
        d[i][0] += d[i-1][1]
    if A[i-1][0] != A[i][1]:
        d[i][1] += d[i-1][0]
    if A[i-1][1] != A[i][1]:
        d[i][1] += d[i-1][1]

    d[i][0] %= mod
    d[i][1] %= mod

print((d[-1][0]+d[-1][1])%mod)