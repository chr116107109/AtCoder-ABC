

N = int(input())

ans = 0

C = 1
for i in range(N-1):
    x = (N-C)/N
    ans += 1/(1-x)
    C += 1

print(ans)