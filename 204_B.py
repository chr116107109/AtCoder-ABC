
N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    ans += max(A[i]-10,0)

print(ans)