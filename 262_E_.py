

N = int(input())
A = list(map(int,input().split()))

d = [[[0 for i in range(j)] for j in range(1,N+1)] for k in range(N)]

mod = 998244353 
ans = N
for i in range(1,N+1):
    d[0][i-1][A[0]%i] = 1

for i in range(1,N):
    for j in range(i,0,-1):
        for k in range(N):
            for l in range(k+1):
                d[j][k][(l+A[i])%(k+1)] += d[j-1][k][l]
                d[j][k][(l+A[i])%(k+1)] %= mod
    
    for j in range(N):
        d[0][j][A[i]%(j+1)] += 1
    
    #print(*d,sep="\n")
    #print("")
ans = 0
for i in range(N):
    ans += d[i][i][0]
    ans %= mod

print(ans)