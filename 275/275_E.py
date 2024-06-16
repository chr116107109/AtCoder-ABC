
N,M,K = map(int,input().split())

d = [[0]*(N+1) for i in range(K+1)]

d[0][0] = 1
ans = 0
P = 998244353 
M_inv = pow(M,P-2,P)
for i in range(K):
    for j in range(0,N):

        for l in range(1,M+1):
            if j+l > N:
                d[i+1][N-(j+l-N)] += d[i][j]*M_inv
                d[i+1][N-(j+l-N)] %= P
            else:
                d[i+1][j+l] += d[i][j]*M_inv
                d[i+1][j+l] %= P

    ans += d[i+1][N]
    ans %= P

print(ans)