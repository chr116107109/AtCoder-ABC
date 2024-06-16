import sys

[N,X] = list(map(int,input().split()))

ab = [list(map(int,input().split())) for _ in range(N)]

a = 0
b = 0
for i in range(N):
    a += ab[i][0]
    b += ab[i][1]

ab = sorted(ab,reverse=True)

if X < a or X > b:
    print('No')
    sys.exit()
elif X == a or X == b:
    print('Yes')
    sys.exit()

d_old = [ab[0][0],ab[0][1]]
d_new = []

for i in range(1,N):
    for j in d_old:
        for k in range(2):
            if j + ab[i][k] > X or j + ab[i][k] in d_new:
                continue
            else:
                d_new.append(j + ab[i][k])
    
    #print(d_new)
    d_old = d_new.copy()
    d_new = []


if X in d_old:
    print('Yes')
else:
    print('No')
