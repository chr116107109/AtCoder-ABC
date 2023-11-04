
H,W,K = map(int,input().split())

S = [input() for i in range(H)]

N = 2**(H+W)

ans = 0
for i in range(N):
    count = 0
    for j in range(H):
        for k in range(W):
            if i & (1 << j) == 0 and i & (1 << (H+k)) == 0 and S[j][k] == '#':
                count += 1
    
    if count == K:
        ans += 1

print(ans)