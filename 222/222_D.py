from itertools import accumulate


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
P = 998244353 
M = 4000
d = [[0]*M for i in range(N)]

for i in range(M):
    if A[0] <= i <= B[0]:
        d[0][i] = 1

comm = list(accumulate(d[0]))

for i in range(1,N):
    for j in range(M):
        if A[i] <= j <= B[i]:
            d[i][j] += comm[j]%P
            d[i][j] %= P
    comm = list(accumulate(d[i]))

ans = 0
for i in range(M):
    ans += d[N-1][i]%P
    ans %= P

print(ans)
