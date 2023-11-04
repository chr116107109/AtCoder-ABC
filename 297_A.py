
N,D = map(int,input().split())
A = list(map(int,input().split()))

ans = -1
for i in range(N-1):
    if A[i+1] - A[i] <= D:
        ans = A[i+1]
        break

print(ans)