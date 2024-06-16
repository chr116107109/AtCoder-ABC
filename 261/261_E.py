

N,C = map(int,input().split())

M = 30
d0 = [[0] * M for j in range(N+1)]
d1 = [[1] * M for j in range(N+1)]

Cl = [0] * M
for i in range(M):
    if C&(1<<i) != 0:
        Cl[i] = 1

ans = []
for i in range(1,N+1):
    T,A = map(int,input().split())
    
    Al = [0] * M
    for j in range(M):
        if A&(1<<j) != 0:
            Al[j] = 1
    
    if T == 1:
        for j in range(M):
            d0[i][j] = d0[i-1][j] * Al[j]
            d1[i][j] = d1[i-1][j] * Al[j]
    if T == 2:
        for j in range(M):
            if d0[i-1][j]==0 and Al[j] == 0:
                d0[i][j] = 0
            else:
                d0[i][j] = 1
            if d1[i-1][j]==0 and Al[j] == 0:
                d1[i][j] = 0
            else:
                d1[i][j] = 1
    if T == 3:
        for j in range(M):
            if d0[i-1][j] == Al[j]:
                d0[i][j] = 0
            else:
                d0[i][j] = 1
            if d1[i-1][j] == Al[j]:
                d1[i][j] = 0
            else:
                d1[i][j] = 1

    C = 0
    for j in range(M):
        if Cl[j] == 1:
            C += (1<<j)*d1[i][j]
            Cl[j] = d1[i][j]
        elif Cl[j] == 0:
            C += (1<<j)*d0[i][j]
            Cl[j] = d0[i][j]


    ans.append(C)


print(*ans, sep='\n')