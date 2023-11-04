
N = int(input())
A = list(map(int,input().split()))

d = [[0,0] for i in range(N)]

d[0][0] = A[0]
d[0][1] = -A[0]

for i in range(1,N-1):
    d[i][0] = max(d[i-1][0]+A[i], d[i-1][1]-A[i])
    d[i][1] = max(d[i-1][0]-A[i], d[i-1][1]+A[i])

d[N-1][0] = d[N-2][0] + A[N-1]
d[N-1][1] = d[N-2][1] - A[N-1]


print(max(d[-1]))