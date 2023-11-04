

N,M = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]

ans = -10**20
for bit in range(8):
    a,b,c = -1,-1,-1
    if bit&(1<<2) != 0:
        a = 1
    if bit&(1<<1) != 0:
        b = 1
    if bit&(1<<0) != 0:
        c = 1
    d = [[-10**20 for i in range(M+1)] for j in range(N+1)]
    d[0][0] = 0
    for i in range(1,N+1):
        d[i][0] = 0
        p = a*A[i-1][0] + b*A[i-1][1] + c*A[i-1][2]
        for j in range(1,M+1):
            d[i][j] = max(d[i-1][j], d[i-1][j-1] + p)

            
    score = d[-1][-1]
    #print(d)
    #print(score,a,b,c)
    ans = max(score,ans)

print(ans)