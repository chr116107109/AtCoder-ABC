
[N,M] = list(map(int,input().split()))

inf = 10**10
d = [[inf]*N for _ in range(N)]
g = [[-1]*N for _ in range(N)]


for i in range(N):
    d[i][i] = 0
    g[i][i] = 0

for i in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
    g[a-1][b-1] = c
    g[b-1][a-1] = c
    

def WFM(d,N,M):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])                    

    return d

d = WFM(d,N,M)

ans = 0
for i in range(N):
    for j in range(N):
        frag = 0
        for k in range(N):
            if frag == 0 and i != j and i != k and j != k and g[i][j] >= d[i][k] + d[k][j]:
                #print(i,j,k)
                ans += 1
                frag = 1

print(ans//2)
