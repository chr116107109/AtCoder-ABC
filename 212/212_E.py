

N,M,K = map(int,input().split())

g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

d = [[0]*N for i in range(K+1)]

d[0][0] = 1
D = 1
mod = 998244353 
for i in range(1,K+1):

    for j in range(N):
        d[i][j] = D - d[i-1][j]
        d[i][j] %= mod
        for k in g[j]:
            d[i][j] -= d[i-1][k]
            d[i][j] %= mod

    D = 0
    for j in range(N):
        D += d[i][j]
        D %= mod

print(d[-1][0])