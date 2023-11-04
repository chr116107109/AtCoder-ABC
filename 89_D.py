

H,W,D = map(int,input().split())

A = [list(map(int,input().split())) for i in range(H)]

B = {}
for i in range(H):
    for j in range(W):
        B[A[i][j]-1] = (i,j)

d = [[[-1,-1,0]] for i in range(D)]

for i in range(H*W):
    mod = i%D
    x,y = B[i]
    if d[mod][-1][0] < 0:
        d[mod].append([x,y,x+y])
    else:
        s,t,v = d[mod][-1]
        d[mod].append([x,y,v+abs(x-s)+abs(y-t)])

Q = int(input())

for i in range(Q):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    print(d[r%D][r//D+1][2]-d[l%D][l//D+1][2])