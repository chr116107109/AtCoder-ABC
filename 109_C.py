

N,X = map(int,input().split())

A = list(map(int,input().split()))
A.append(X)
A.sort()
import math

ans = A[1]-A[0]

for i in range(1,N+1):
    ans = math.gcd(ans,abs(A[i]-A[i-1]))

print(ans)