
N = int(input())
A = list(map(int,input().split()))

x = [0] * N
x[0] = sum([(-1)**i * A[i] for i in range(N)])
for i in range(1,N):
    x[i] = 2*(A[i-1] - x[i-1]//2)

print(*x)