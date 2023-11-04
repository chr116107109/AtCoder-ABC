
H,N = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

inf = 10**10
d = [[inf]*(H+1) for i in range(N)]

d[0][0] = 0
i = 0
while i <= H :
    i += A[0][0]
    d[0][min(i,H)] = min(d[0][min(i,H)], d[0][i-A[0][0]] + A[0][1])

for i in range(1,N):
    for j in range(H+1):
        d[i][j] = d[i-1][j]
    for j in range(H):
        d[i][min(j+A[i][0],H)] = min(d[i][min(j+A[i][0],H)], d[i][j]+A[i][1])

print(d[-1][H])