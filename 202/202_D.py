import math

A,B,K = map(int,input().split())

rank = 0
ans = ''
while A > 0 and B > 0:
    if rank + math.comb(A+B-1,A-1) < K:
        ans += 'b'
        rank += math.comb(A+B-1,A-1)
        B -= 1
    else:
        ans += 'a'
        A -= 1

ans += 'a' * A + 'b' * B

print(ans)