

N,M = map(int,input().split())
A = list(map(int,input().split()))

dp = [[-10**20] * M for i in range(N)]

dp[0][0] = A[0]

for i in range(1,N):
    for j in range(min(i+1,M)):
        if j == 0:
            dp[i][j] = max(dp[i-1][j], A[i])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (j+1) * A[i])


print(dp[N-1][M-1])