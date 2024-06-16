
N,M = map(int,input().split())
A = list(map(int,input().split()))

g = [[set(),set()] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1][0].add(b-1)
    g[b-1][1].add(a-1)

inf = 10**10
din = [inf] * N
dout = [-inf] * N

for i in range(N):
    din[i] = min(A[i],din[i])
    for j in g[i][0]:
        din[j] = min(din[j],din[i])
    

for i in range(N-1,-1,-1):

    for j in g[i][1]:
        dout[j] = max(dout[j], A[i], dout[i])

ans = -inf
for i in range(N):
    if din[i] < inf and dout[i] > -inf:
        ans = max(ans, dout[i]-din[i])

print(ans)