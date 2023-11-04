
N,M,K = map(int,input().split())

d = [[0]*K for i in range(N)]
P = 998244353 
for i in range(M):
    d[0][i] = 1

for i in range(1,N):
    for j in range(K):
        for l in range(1,M+1):
            if j+l < K:
                d[i][j+l] = (d[i][j+l] + d[i-1][j])%P

ans = 0
for i in range(K):
    ans = (ans + d[N-1][i])%P

print(ans)