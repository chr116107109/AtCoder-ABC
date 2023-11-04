
X,A,D,N = map(int,input().split())

max_S = max(A + D*(N-1), A)
min_S = min(A + D*(N-1), A)

if X >= max_S:
    print(X - max_S)
elif X < min_S:
    print(min_S - X)
else:
    X = X - A
    ans = min(abs(X%D),abs(D - X%D))
    print(ans)