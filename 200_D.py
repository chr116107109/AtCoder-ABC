
N = int(input())
A = list(map(int,input().split()))

d = [[[] for j in range(200)] for i in range(N)] 

d[0][A[0]%200] = [1]
a = []
b = [] 
for i in range(N-1):
    d[i+1][A[i+1]%200] = [i+2]
    for j in range(200):
        if d[i][j] == []:
            continue
        if d[i+1][j] == []:
            d[i+1][j] = d[i][j]
        else:
            a = d[i][j]
            b = d[i+1][j]
            break

        if d[i+1][(j+A[i+1])%200] == []:
            d[i+1][(j+A[i+1])%200] = d[i][j] + [i+2]
        else:
            a = d[i+1][(j+A[i+1])%200]
            b = d[i][j] + [i+2]
            break

if a == []:
    print('No')
else:
    print('Yes')
    print(len(a),*a)
    print(len(b),*b)