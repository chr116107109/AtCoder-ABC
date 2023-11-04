
import math

N = int(input())
A = list(map(int,input().split()))

A.sort()
target = math.gcd(A[0],A[1])
ans = 0
for i in range(N):
    target = math.gcd(target,A[i])
    

for i in range(N):    
    diff = A[i]//target
    num = 0
    #print(target,diff)
    while diff%2==0:
        diff //= 2
        num += 1
    while diff%3==0:
        diff //= 3
        num += 1
    if diff == 1:
        ans += num
    else:
        ans = -1
        break

print(ans)