

N = int(input())

x = {}
X = {}
y = {}
A = {}

for i in range(N):
    r,c,s = map(int,input().split())
    A[(r,c)] = s

    if r in x:
        x[r] += s
    else:
        x[r] = s
    if c in y:
        y[c] += s
    else:
        y[c] = s
    if r in X:
        X[r].add(c)
    else:
        X[r] = {c}

Y = sorted(y.items(), key=lambda x:x[1])
Y.reverse()

ans = 0

for r in X:
    n = len(X[r])
    for i in range(min(n+1,len(Y))):
        a = x[r] + Y[i][1]
        if Y[i][0] in X[r]:
            a -= A[(r,Y[i][0])]
        ans = max(ans,a)

print(ans)