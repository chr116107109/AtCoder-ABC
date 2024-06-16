
N,K = map(int,input().split())
A = list(map(int,input().split()))

d = [[0] * (K) for i in range(N+1)]

for i in range(1,N+1):
    d[i][0] = (i)//2 + (i)%2
for i in range(N+1):
    for j in range(1,K):
        if i >= A[j]:
            d[i][j] = max(d[i][j], d[i][j-1], A[j] + (i-A[j]) - d[i-A[j]][-1])
        else:
            d[i][j] = d[i][j-1]

print(d[-1][-1])