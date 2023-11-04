
N,M = map(int,input().split())
V = [list(map(int,input().split())) for i in range(N)]
U = [list(map(int,input().split())) for i in range(M)]
NN = 2**(N+M)

inf = 10**20
ans = inf
d = [[inf]*(N+M) for i in range(NN+5)]
#booster = [[0]*(N+M) for i in range(NN+5)]
for i in range(N+M):
    a = V[i] if i < N else U[i-N]
    d[1<<i][i] = (a[0]**2 + a[1]**2)**(1/2)

for i in range(1,NN):
    speed = 1
    for j in range(N,N+M):
        if i&(1<<j) != 0:
            speed *= 2
    for j in range(N+M):
        #print(i,speed)
        if d[i][j] == inf:
            continue
        for k in range(N+M):
            if i&(1<<k) != 0:
                continue
            b = V[j] if j < N else U[j-N]
            a = V[k] if k < N else U[k-N]
            
            L = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
            L /= speed
            t = i|(1<<k)
            if d[t][k] > d[i][j]+L:
                d[t][k] = d[i][j]+L
                
                
            #print(i,j,k,L)
            #print(i|(1<<k))
            #print(d[i][j])
            #print(d[i|(1<<k)][k])
    


for ii in range(2**M):
    i = ii*(2**N) + 2**N-1
        #print(i,d[i])
    speed = 1
    for j in range(N,N+M):
        if i&(1<<j) != 0:
            speed *= 2
    for k in range(N+M):
        a = V[k] if k < N else U[k-N]
        l = (a[0]**2 + a[1]**2)**(1/2)
        l /= speed
        ans = min(ans, d[i][k]+l)

print(ans)