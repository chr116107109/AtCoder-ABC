

N,M,K = map(int,input().split())
A = [list(map(int,input().split())) for i in range(M)]
E = list(map(int,input().split()))

inf = 10**20
d = [inf] * N

d[0] = 0

for i in range(K):
    ind = E[i]-1
    d[A[ind][1]-1] = min(d[A[ind][1]-1], d[A[ind][0]-1] + A[ind][2])
    #print(d)

if d[-1] == inf:
    print(-1)
else:
    print(d[-1])