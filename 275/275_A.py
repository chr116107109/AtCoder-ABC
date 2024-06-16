
N = int(input())
H = list(map(int,input().split()))

ans = 0
M = 0
for i in range(N):
    if H[i] > M:
        M = H[i]
        ans = i+1

print(ans)