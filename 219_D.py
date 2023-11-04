

N = int(input())
[X, Y] = list(map(int, input().split()))


M = 302
inf = 10**10
d = [[inf]*M for i in range(M)]
ans = inf
d[0][0] = 0
for i in range(1,N+1):
    A,B = map(int, input().split())

    for j in range(M-1,-1,-1):
        for k in range(M-1,-1,-1):
            if d[j][k] != inf:
                s = min(M-1,j+A)
                t = min(M-1,k+B)
                
                d[s][t] = min(d[s][t], d[j][k]+1)
                if s >= X and t >= Y:
                    ans = min(ans, d[s][t])

if ans < inf:
    print(ans)
else:
    print(-1)