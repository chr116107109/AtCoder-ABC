
import math
from re import I
N, A, B = map(int, input().split())

ans = (1+N)*N//2

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def sum_n(A, N):
    n = N//A
    A_sum = (1+n)*n*A//2 

    return A_sum 

if A == 1 or B == 1:
    print(0)
else:
    ans = ans - sum_n(A, N) - sum_n(B, N) + sum_n(lcm(A,B), N)
    print(ans)

def test(N,A,B):
    ans = 0
    for i in range(1,N+1):
        if i%A != 0 and i%B != 0:
            ans += i
    
    return ans
