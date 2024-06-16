

N = int(input())

import math
M = 10**5
ans = N
S = set()
for i in range(2,M+1):
            
    a = i*i
    while a <= N:
        if a in S:
            break
        ans -= 1
        S.add(a)
        a *= i

print(ans)

