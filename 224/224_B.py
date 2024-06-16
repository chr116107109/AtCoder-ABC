import sys

[H,W] = list(map(int,input().split()))
A = [list(map(int,input().split())) for i in range(H)]

for i1 in range(H):
    for j1 in range(W):
        for i2 in range(i1+1,H):
            for j2 in range(j1+1,W):
                #print([i1,i2,j1,j2])
                #print(A[i1][j1] + A[i2][j2] - (A[i2][j1] + A[i1][j2]))
                if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                    print('No')
                    sys.exit()


print('Yes')
