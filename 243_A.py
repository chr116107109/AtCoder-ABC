
[V,A,B,C] = list(map(int,input().split()))

X = [A,B,C]
Y = 'FMT'
now = 0
while V >= 0:
    if V < X[now]:
        print(Y[now])
        V -= X[now]
    else:
        V = V - X[now]
        now = (now+1)%3