

N = int(input())
A = list(map(int,input().split()))

B = [0] * (N+1)
for i in range(1,N+1):
    B[i] = B[i-1] + A[i-1]

ans = 0

for i in range(N):
    ans += A[i]*(B[-1]-B[i+1])
    ans %= 10**9+7

print(ans)