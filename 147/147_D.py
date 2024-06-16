


N = int(input())
A = list(map(int,input().split()))

d = [[0]*60 for i in range(N+1)]

for i in range(1,N+1):
    for j in range(60):
        d[i][j] = d[i-1][j]
        if A[i-1]&(1<<j) != 0:
            d[i][j] += 1

ans = 0
mod = 10**9+7
for i in range(1,N+1):
    p = 1
    for j in range(60):
        if A[i-1]&(1<<j) != 0:
            ans += (N-i-(d[-1][j]-d[i][j])) * p
            ans %= mod
        else:
            ans += (d[-1][j]-d[i][j]) * p
            ans %= mod
        p *= 2
        p %= mod

print(ans)