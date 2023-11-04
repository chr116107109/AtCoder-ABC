
N,M,Q = map(int,input().split())
obj = [list(map(int,input().split())) for i in range(N)]
obj.sort(key=lambda x:-x[1])    
X = list(map(int,input().split()))
for i in range(Q):
    L,R = map(int,input().split())
    Y = X[:L-1] + X[R:]
    #print(Y)
    ans = 0
    is_fill = [False] * len(Y)
    for b in obj:
        w = (10**7,-1)
        for j,x in enumerate(Y):
            if b[0] <= x and x < w[0] and not is_fill[j]:
                w = (x,j)
        if w[1] > -1:
            is_fill[w[1]] = True
            ans += b[1]
        if len([f for f in is_fill if f]) == len(Y):
            break
        #print(is_fill)

    print(ans)