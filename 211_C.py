import itertools
S = input()
N = len(S)
d = [[0] * N for i in range(8)]
P = (10**9+7)
A = 'chokudai'
for i in range(N):
    if S[i] == 'c':
        d[0][i] += 1
B = list(itertools.accumulate(d[0]))
for i in range(1,8):
    for j in range(1,N):
        if S[j] == A[i]:
            d[i][j] += B[j-1]
            d[i][j] %= P
    B = list(itertools.accumulate(d[i]))

print(B[-1]%P)
