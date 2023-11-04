
S = input()
N = len(S)
S = S[::-1]
P =10**9+7
d = [[0] * 13 for i in range(N)]

mod13 = {}
for i in range(N-1):
    mod13[i] = pow(10,i+1,13)

if S[0] == '?':
    for i in range(10):
        d[0][i] = 1
else:
    d[0][int(S[0])] = 1
for i in range(N-1):
    for j in range(13):

        if S[i+1] == '?':
            for k in range(10):
                d[i+1][(j+k*mod13[i])%13] += d[i][j]
                d[i+1][(j+k*mod13[i])%13] %= P
        else:
            d[i+1][(j+int(S[i+1])*mod13[i])%13] += d[i][j]
            d[i+1][(j+int(S[i+1])*mod13[i])%13] %= P

print(d[-1][5])
