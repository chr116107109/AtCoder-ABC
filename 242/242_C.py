
N = int(input())

p = 998244353
d = [[1] * 9 for i in range(N)]
for i in range(1,N):
    for j in range(9):
        if j == 0:
            d[i][j] = (d[i-1][j] + d[i-1][j+1]) % p
        elif j == 8:
            d[i][j] = (d[i-1][j] + d[i-1][j-1]) % p
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j] + d[i-1][j+1]) % p


ans = sum(d[N-1]) % p
print(ans)