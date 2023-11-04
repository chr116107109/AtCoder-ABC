
N,X,M = map(int,input().split())

before_loop = []
visited = set()

A = X
def f(a):
    return (a*a)%M
while not A in visited:
    before_loop.append(A)
    visited.add(A)
    A *= A
    A %= M

loop = [A]
start = A
while f(A) != start:
    A = f(A)
    loop.append(A)


if N <= len(before_loop):
    ans = 0
    A = X
    for i in range(N):
        ans += X
        X = f(X)

else:
    ans = 0

    ans += sum(before_loop)
    N -= len(before_loop)
    ans += (N//len(loop)) * sum(loop)
    N %= len(loop)
    A = start
    for i in range(N):
        ans += A
        A = f(A)

print(ans)