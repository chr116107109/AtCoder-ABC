


N = int(input())
A = list(map(int,input().split()))

g = [[] for i in range(N)]
inf = 10**20
d = [[inf for i in range(N)] for i in range(N)]
f = [[0 for i in range(N)] for i in range(N)]
for i in range(N):
    S = input()
    for j in range(N):
        if S[j] == 'Y':
            d[i][j] = 1
            f[i][j] = A[i]+A[j]

def WFM():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    f[i][j] = f[i][k] + f[k][j] - A[k]
                elif d[i][j] == d[i][k] + d[k][j]:
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] - A[k])
    return d

WFM()
Q = int(input())
for i in range(Q):
    U,V = map(int,input().split())
    if d[U-1][V-1] == inf:
        print('Impossible')
    else:
        print(d[U-1][V-1], f[U-1][V-1])

