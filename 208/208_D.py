
N,M = map(int,input().split())
inf = 10**10
d = [[inf]*(N) for i in range(N)]
ans = 0
for i in range(N):
    d[i][i] = 0
for i in range(M):
    A,B,C = map(int,input().split())
    d[A-1][B-1] = C

for k in range(N):
    for s in range(N):
        for t in range(N):
            if s == t:
                continue
            d[s][t] = min(d[s][t], d[s][k] + d[k][t])
            if d[s][t] < inf:
                ans += d[s][t]
    #print(d)
print(ans)

