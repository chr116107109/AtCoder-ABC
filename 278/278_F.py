

N = int(input())

S = [input() for i in range(N)]
d = [[0]*26 for i in range(2**(N))]

win = [0] * (2**N)

for i in range(N):
    j = ord(S[i][0])-97
    d[1<<i][j] = 1
    win[1<<i] = 1

for bit in range(2**(N)):
    for i in range(N):
        if bit & (1<<i) != 0:
            continue
        j = ord(S[i][0]) - 97
        k = ord(S[i][-1]) - 97
        d[bit | (1<<i)][j] = max(d[bit | (1<<i)][j], (d[bit][k] + 1)%2)

if 1 in d[-1]:
    print('First')
else:
    print('Second')
