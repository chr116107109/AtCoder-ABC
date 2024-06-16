
N,M,K,S,T,X = map(int,input().split())
P = 998244353

E = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())

    E[u-1].append(v-1)
    E[v-1].append(u-1)


d = [[0]*N for i in range(K+1)] # 偶数

f = [[0]*N for i in range(K+1)] # 奇数

if S == X:
    f[0][S-1] = 1
else:
    d[0][S-1] = 1

for i in range(1,K+1):
    for j in range(N):
        for e in E[j]:
            if e == X-1:
                f[i][j] = (f[i][j]+d[i-1][e])%P
                d[i][j] = (d[i][j]+f[i-1][e])%P
            
            else:
                f[i][j] = (f[i][j]+f[i-1][e])%P
                d[i][j] = (d[i][j]+d[i-1][e])%P

print(d[K][T-1]%P)