
N,K = map(int,input().split())
A = list(map(int,input().split()))
XY = [list(map(int,input().split())) for i in range(N)]

dist = 0
for i in range(N):
    [x,y] = XY[i]
    d = 10**20
    for j in range(K):
        d = min(d,(XY[A[j]-1][0]-x)**2 + (XY[A[j]-1][1]-y)**2)
        #print((XY[A[j]-1][0]-x)**2 + (XY[A[j]-1][1]-y)**2)
    #print(d)
    dist = max(dist,d)

print(dist**(1/2))