

[N,K,A] = list(map(int,input().split()))

ans = A
for i in range(K-1):
    #print(ans)
    ans = ans + 1
    if ans == N + 1:
        ans = 1


print(ans)
