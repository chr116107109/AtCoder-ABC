
H,W,M = map(int,input().split())

tate = [0] * H
yoko = [0] * W

B = set()
for i in range(M):
    h,w = map(int,input().split())
    tate[h-1] += 1
    yoko[w-1] += 1
    B.add((h-1,w-1))

T = 0
ind = []
for i in range(H):
    T = max(T,tate[i])
for i in range(H):
    if tate[i] == T:
        ind.append(i)

Y = 0
indd = []
for i in range(W):
    Y = max(Y,yoko[i])
for i in range(W):
    if yoko[i] == Y:
        indd.append(i)

ans = 0
for i in ind:
    for j in indd:
        if (i,j) in B:
            ans = max(ans,T+Y-1)
        else:
            ans = max(ans,T+Y)
            break

print(ans)