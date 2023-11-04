
N = int(input())
a = list(map(int,input().split()))

d = [[[[0]*(l+1) for l in range(N)] for k in range(i+2)] for i in range(N)]

d[0][0][0][0] = 1

P = 998244353

for l in range(1,N):
    for m in range(l+1):
        if a[0]%(l+1) == m:
            d[0][0][l][m] += 1
        

for i in range(1,N):
    for l in range(N):
        for m in range(l+1):
            if a[i]%(l+1) == m:
                d[i][0][l][m] = (d[i-1][0][l][m] + 1)%P
            else:
                d[i][0][l][m] = d[i-1][0][l][m]

    for k in range(1,i+1):
        for l in range(N):
            for m in range(l+1):
                d[i][k][l][m] += d[i-1][k][l][m]
                d[i][k][l][(a[i]+m)%(l+1)] = (d[i][k][l][(a[i]+m)%(l+1)]+d[i-1][k-1][l][m])%P


ans = sum([d[N-1][k][k][0] for k in range(N)])

print(ans%P)
