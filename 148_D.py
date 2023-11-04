
N = int(input())
A = list(map(int,input().split()))

target = 1
ans = 0
for i in range(N):
    if target != A[i]:
        ans += 1
    else:
        target += 1

if target == 1:
    print(-1)
else:
    print(ans)