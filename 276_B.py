
N,M = map(int,input().split())
g = [[] for i in range(N+1)]
for i in range(M):
    A,B = map(int,input().split())
    g[A].append(B)
    g[B].append(A)

for i in range(1,N+1):
    ans = [len(g[i])] + sorted(g[i])
    print(*ans)
    
