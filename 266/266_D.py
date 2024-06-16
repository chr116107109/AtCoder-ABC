
N = int(input())

M = 10*2
d = [[0] * 5 for i in range(M)]

T,X,A = map(int,input().split())
for i in range(M):
    for j in range(5):
        d[i][j] = max(d[i-1][j],d[i-1][min(j+1,4)],d[i-1][max(j-1,0)])

    if i == T:
        if i-X >= 0:
            d[i][X] += A

        N -= 1
        if N == 0:
            break
        T,X,A = map(int,input().split())

print(max([d[T][i] for i in range(5)]))