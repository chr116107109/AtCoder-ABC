

N,K,D = map(int,input().split())
A = list(map(int,input().split()))

ans = -1

d = [[[-1 for k in range(D)] for i in range(K+1)] for j in range(N+1)]

d[0][0][0] = 0

for i in range(N):
    for j in range(K+1):
        for k in range(D):
            if d[i][j][k] == -1:
                continue
            d[i+1][j][k] = max(d[i+1][j][k],d[i][j][k])

            #if d[i+1][j+1][(k+A[i])%D] < d[i][j][k] + A[i]: 
            if j!=K:
                d[i+1][j+1][(k+A[i])%D] = max(d[i+1][j+1][(k+A[i])%D],d[i][j][k] + A[i])

            #print(i,j,k)
            #print(d) 
print(d[N][K][0])