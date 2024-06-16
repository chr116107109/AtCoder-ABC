

N,M = map(int,input().split())

NN = 10**6 + 10

ans = -1
for i in range(1,min(N,NN)+1):
    if M%i == 0 and M//i <= N:
        ans = M
        break
    elif (M//i+1) <= N:
        if ans > 0:
            ans = min(ans,(M//i+1)*i)
        else:
            ans = (M//i+1)*i

print(ans)