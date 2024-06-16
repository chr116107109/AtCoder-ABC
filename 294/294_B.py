
H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]

S = [['']*W for i in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == 0:
            S[i][j] = '.'
        else:
            S[i][j] = chr(64+A[i][j])

for i in range(H):
    print("".join(S[i]))