
N = int(input())
T = list(map(int,input().split()))
M = sum(T)

d = [[0]*(M+1) for i in range(N)]
d[0][T[0]] = 1
for i in range(1,N):
    d[i][T[i]] = 1
    for j in range(M):
        if d[i-1][j] == 1:
            d[i][j] = 1
            d[i][j+T[i]] = 1

for i in range(M//2,M+1):
    #print(i,d[N-1][i])
    if i < M/2:
        continue
    if d[N-1][i] == 1:
        print(i)
        break
