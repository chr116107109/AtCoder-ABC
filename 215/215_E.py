
N = int(input())
S = input()
mod = 998244353
def f(s):
    return ord(s)-65

d = [[[0] * 11 for i in range(2**10+1)] for j in range(N)]


d[0][1<<(f(S[0]))][f(S[0])] += 1

ans = 0
for i in range(1,N):
    d[i][1<<(f(S[i]))][f(S[i])] = 1
    for j in range(2**10):
        for k in range(10):
            d[i][j][k] += d[i-1][j][k]
            d[i][j][k] %= mod
            if j & (1<<f(S[i])) != 0:
                if k == f(S[i]):
                    d[i][j][k] += d[i-1][j][k]
                    d[i][j][k] %= mod
                continue
            d[i][j|(1<<f(S[i]))][f(S[i])] += d[i-1][j][k]
            d[i][j|(1<<f(S[i]))][f(S[i])] %= mod
for j in range(2**10):
    for k in range(10):
        ans += d[-1][j][k]
        ans %= mod

print(ans)