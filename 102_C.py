

N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    A[i] -= i

A.sort()

a = A[N//2]
if N//2+1 < N:
    b = A[N//2+1]

ans = 10**20
ans = min(ans,sum(abs(A[i]-a) for i in range(N)))
if N//2+1<N:
    ans = min(ans,sum(abs(A[i]-b) for i in range(N)))

print(ans)