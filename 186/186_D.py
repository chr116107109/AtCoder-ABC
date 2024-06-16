

N = int(input())
A = list(map(int,input().split()))
A.sort()

B = sum(A)
ans = 0

for i in range(N):
    ans += B-A[i]*(N-i)
    B -= A[i]

print(ans)