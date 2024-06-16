
N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

Y = sum(a[0] for a in A)

A.sort(key=lambda x:(2*x[0]+x[1]))

X = 0
while X <= Y and A:
    a,b = A.pop()
    X += a+b
    Y -= a

print(N-len(A))