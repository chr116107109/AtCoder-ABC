
N,M,T = map(int,input().split())
A = list(map(int,input().split()))
d = {}
for i in range(M):
    X,Y = map(int,input().split())
    d[X-1] = Y

now = 0
ans = 'Yes'
while T > 0 and now < N-1:
    if now in d:
        T += d[now]
    if A[now] < T:
        T -= A[now]
        now += 1
    else:
        ans = 'No'
        break

print(ans)