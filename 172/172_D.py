
N = int(input())

ans = 0
for K in range(1,N+1):
    ans += (K+K*(N//K))*((N//K))//2

print(ans)