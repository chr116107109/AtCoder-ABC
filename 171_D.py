from collections import Counter

N = int(input())
A = list(map(int,input().split()))
Q = int(input())

C = Counter(A)
ans = sum(A)
for i in range(Q):
    X,Y = map(int,input().split())
    if X in C:
        C[Y] += C[X]
        ans += Y*C[X]
        ans -= X*C[X]
        C[X] = 0

    print(ans)
