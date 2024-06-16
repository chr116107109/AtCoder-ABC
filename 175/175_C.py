
X,K,D = map(int,input().split())

if X < 0:
    X *= -1

if K < X//D:
    print(X-K*D)
else:
    if (K-X//D)%2 == 0:
        print(X%D)
    else:
        print(abs(X%D - D))

