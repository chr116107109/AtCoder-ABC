

[N, A, X, Y] = list(map(int, input().split()))


if N<=A:
    P = N*X
else:
    P = A*X + (N-A)*Y

print(P)
