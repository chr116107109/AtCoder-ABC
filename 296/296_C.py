
N,X = map(int,input().split())
A = list(map(int,input().split()))

B = set(A)

ans = "No"
for i in range(N):
    if A[i] + X in B:
        ans = "Yes"

print(ans)