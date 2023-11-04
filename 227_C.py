
N = int(input())

ans = 0

for i in range(1,N+1):
    if i*i*i > N:
        break
    for j in range(i,N+1):
        if i*j*j > N:
            break
        ab = i*j
        M = N // ab
        #print([i,j,M])
        ans += (M - j + 1)

print(ans)
