

N = int(input())

N *= 2
M = int(N**(1/2))

ans = 0
for i in range(1,M+1):
    if N%i == 0:
        
        if (N//i-i+1)%2 == 0:
            ans += 1
            #print((N//i-i+1)//2)
        if (i-N//i+1)%2 == 0:
            ans += 1
            #print((i-N//i+1)//2)

print(ans)