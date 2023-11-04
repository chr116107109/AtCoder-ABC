
N,X = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

d = [False] * (X+1)

d[0] = True

for i in range(N):
    for j in range(X, -1, -1):
        if d[j]:    
            for k in range(1,A[i][1]+1):
                if j+A[i][0]*k > X:
                    break
                d[j+A[i][0]*k] = True

if d[-1]:
    print('Yes')
else:
    print('No')