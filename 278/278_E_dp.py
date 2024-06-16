
H,W,N,h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
import copy
d = [[[0] * (N+1) for j in range(W+1)] for i in range(H+1)]

def union_(a,b):
    for k in range(N+1):
        a[k] += b[k]

def diff_(a,b):
    for k in range(N+1):
        a[k] -= b[k]

for i in range(1,H+1):
    for j in range(1,W+1):
        union_(d[i][j],d[i-1][j])
        union_(d[i][j],d[i][j-1])
        diff_(d[i][j],d[i-1][j-1])
        d[i][j][A[i-1][j-1]] += 1 

for i in range(H-h+1):
    q = []
    ans = copy.deepcopy(d[H][W])
    diff_(ans,d[i+h][w])
    union_(ans,d[i][w])
    for j in range(W-w+1):
        count = 0
        #print(ans)
        for k in range(N+1):
            if ans[k] > 0:
                count += 1
        q.append(count)
        if j == W-w:
            break
        for k in range(h):
            ans[A[i+k][j+w]] -= 1
            ans[A[i+k][j]] += 1
        

    print(*q)





