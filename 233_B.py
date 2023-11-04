

[L,R] = list(map(int,input().split()))
S = input()

ans = ''

ans += S[:L-1]
M = S[L-1:R]
ans += M[::-1]
ans += S[R:]

print(ans)
