

N,K = map(int,input().split())

H = [int(input()) for i in range(N)]

H.sort()
hmin = H[0]
hmax = H[K-1]
ans = hmax-hmin
for i in range(1,N-K+1):
    hmin = H[i]
    hmax = H[K-1+i]
    ans = min(ans,hmax-hmin)

print(ans)