
N = int(input())
A = list(map(int,input().split()))

B = [0] * N
for i in range(N):
    for j in range(i+1):
        ind = min(j,i-j)
        B[i] += A[ind]

d = [0] * N

for i in range(N):
    if i+1 < N:
        d[i+1] = max(d[i+1],B[i])
    for j in range(N):
        if i+j+2 < N:
            d[i+j+2] = max(d[i+j+2], d[j] + B[i])


print(max(d))