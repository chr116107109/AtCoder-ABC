
H,W = map(int,input().split())
S = [input() for i in range(H)]

d = [[0]*W for i in range(H)]
a = [[0]*(W+1) for i in range(H+1)]
b = [[0]*(W+1) for i in range(H+1)]
c = [[0]*(W+1) for i in range(H+1)]

mod = 10**9+7

d[0][0] = 1
a[1][1] = 1
b[1][1] = 1
c[1][1] = 1
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        if i == 0 and j == 0 :
            continue
        
        d[i][j] = a[i][j] + b[i][j+1] + c[i+1][j]
        d[i][j] %= mod

        a[i+1][j+1] = a[i][j] + d[i][j]
        a[i+1][j+1] %= mod 
        b[i+1][j+1] = b[i][j+1] + d[i][j]
        b[i+1][j+1] %= mod
        c[i+1][j+1] = c[i+1][j] + d[i][j]
        c[i+1][j+1] %= mod
        #print(d)
        

print(d[-1][-1])

