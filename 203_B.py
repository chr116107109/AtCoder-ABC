

N,K = map(int,input().split())

ans = 0
for i in range(1,N+1):
    for j in range(1,K+1):
        ans += 100*i+j

print(ans)    