
H,W = map(int,input().split())
C = [input() for i in range(H)]

X = [0] * W

for i in range(H):
    for j in range(W):
        if C[i][j] == '#':
            X[j] += 1

print(*X)