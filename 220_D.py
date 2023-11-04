

N = int(input())
A = list(map(int,input().split()))

d = [[0]*10 for i in range(N)]

d[0][A[0]] = 1


for n in range(1,N):

    for j in range(10):
        f = (j+A[n])%10
        g = (j*A[n])%10
        #print(f,g)
        d[n][f] += d[n-1][j] % 998244353
        d[n][g] += d[n-1][j] % 998244353

    #print(d)

for i in range(10):
    print(d[N-1][i]% 998244353)
