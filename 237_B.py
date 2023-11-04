
[H,W] = list(map(int,input().split()))

A = [list(map(int,input().split())) for i in range(H)]

B = [[0] * H for i in range(W)]

for i in range(W):
    for j in range(H):
        B[i][j] = A[j][i]

for i in range(W):
    print(*B[i])
