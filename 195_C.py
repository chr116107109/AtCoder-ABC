

N = int(input())

M = 10**3

ans = 0
while N >= M:
    ans += N - M + 1
    M *= 10**3

print(ans)
