

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

C = [[] for i in range(N+1)]
for i in range(N):
    C[A[i-1][1]].append(A[i-1][0])

inf = 10**20
d = [[inf,inf] for i in range(N+1)]

now = [0,0]
d[0] = [0,0]
for i in range(1,N+1):
    l,r = min(now),max(now)

    if C[i] == []:
        d[i] = d[i-1][:]
        continue

    d[i][0] = min(d[i-1][0]+abs(l-r)+abs(min(C[i])-r), d[i-1][1]+abs(l-r)+abs(min(C[i])-l))
    d[i][1] = min(d[i-1][0]+abs(l-r)+abs(max(C[i])-r), d[i-1][1]+abs(l-r)+abs(max(C[i])-l))

    now = [min(C[i]),max(C[i])]

ans = min(d[N][0]+abs(now[0]-now[1])+abs(now[1]), d[N][1]+abs(now[1]-now[0])+abs(now[0]))

print(ans)