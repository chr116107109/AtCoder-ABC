

N,T = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]

A.sort(key=lambda x:x[0])

d = [[0]*(T+A[-1][0]) for i in range(N+1)]

for i in range(N):

    for j in range(T+A[-1][0]):
        d[i+1][j] = d[i][j]
    for j in range(T):
        d[i+1][j+A[i][0]] = max(d[i+1][j+A[i][0]], d[i][j]+A[i][1])

print(max(d[-1]))