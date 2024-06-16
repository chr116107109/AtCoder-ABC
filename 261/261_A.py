
A = list(map(int,input().split()))

ans = 0
for i in range(1000):
    if A[0] < i <= A[1] and A[2] < i <= A[3]:
        ans += 1

print(ans)