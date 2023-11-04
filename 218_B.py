

S = 'abcdefghijklmnopqrstuvwxyz'

P = list(map(int, input().split()))

ans = ['a'] * 26
for i in range(26):
    ans[i] = S[P[i] - 1]

print(*ans,sep = '')
