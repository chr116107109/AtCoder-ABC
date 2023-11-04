
H,W = map(int,input().split())
A = [input() for i in range(H)]

ans = [0] * min(H,W)
for j in range(W):

    l = 0
    for k in range(min(H,W)):
        if j+k >= W or k >= H:
            break
        if A[k][j+k] == '#':
            l += 1
        elif A[k][j+k] == '.' and l > 1:
            ans[(l-1)//2-1] += 1
            l = 0
        else:
            l = 0
    if l > 1:
        ans[(l-1)//2-1] += 1
            

for i in range(1,H):

    l = 0
    for k in range(min(H,W)):
        if i+k >= H or k >= W:
            break
        if A[i+k][k] == '#':
            l += 1
        elif A[i+k][k] == '.' and l > 1:
            ans[(l-1)//2-1] += 1
            l = 0
        else:
            l = 0
    if l > 1:
        ans[(l-1)//2-1] += 1

print(*ans)