

N = int(input())

A = list(map(int,input().split()))

A1 = 0
A2 = 0
A3 = 0
B = 0
C = 0
for i in range(2,N+1):
    A1 += (i-1)*(A[i-1]**2)
    B += A[i-2]
    C += A[i-2]**2

    A2 += C
    A3 += A[i-1]*B




ans = A1 + A2 - 2*A3

print(ans)
