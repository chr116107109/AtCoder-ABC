
X,Y,Z = map(int,input().split())

if X < Y < 0:
    if Z < Y:
        print(-1)
    elif Z > 0:
        print(2*Z+abs(X))
    else:
        print(abs(X))
elif X > Y > 0:
    if Z > Y:
        print(-1)
    elif Z < 0:
        print(2*abs(Z)+X)
    else:
        print(X)
else:
    print(abs(X))
