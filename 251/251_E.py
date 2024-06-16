
N = int(input())
A = list(map(int,input().split()))

d = [0] * N

d[0] = A[0]
d[1] = A[0]

for i in range(N-2):
    d[i+2] = min(d[i]+A[i+1],d[i+1]+A[i+2])

ans = d[-1]

d = [0] * N

d[-1] = A[-1]
d[0] = A[-1]


for i in range(N-2):
    d[i+1] = min(d[i-1]+A[i],d[i]+A[i+1])

ans = min(ans,d[-2])

print(ans)