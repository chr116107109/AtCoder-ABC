

N,S = map(int,input().split())

d = [['']*(S+1) for i in range(N)]

a,b = map(int,input().split())
if a <= S:
    d[0][a] = 'H'
if b <= S:
    d[0][b] = 'T'
for i in range(1,N):
    a,b = map(int,input().split())
    for j in range(S):
        if d[i-1][j] != '':
            if j+a <= S:
                d[i][j+a] = d[i-1][j]+'H'
            if j+b <= S:
                d[i][j+b] = d[i-1][j]+'T'

if d[N-1][S] != '':
    print('Yes',d[N-1][S])
else:
    print('No')