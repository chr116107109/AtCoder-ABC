
X,Y,N = map(int,input().split())

if X > Y//3:
    print((N//3) * Y + (N%3) * X)
else:
    print(N*X)