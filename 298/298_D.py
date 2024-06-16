

Q = int(input())

from collections import deque
S = deque()
S.append(1)
ans = 1
mod = 998244353 

for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        S.append(q[1])
        ans *= 10
        ans += q[1]
        ans %= mod
    if q[0] == 2:
        n = len(S)
        fast = S.popleft()
        ans -= fast*pow(10,n-1,mod)
        ans %= mod
    if q[0] == 3:
        print(ans)

