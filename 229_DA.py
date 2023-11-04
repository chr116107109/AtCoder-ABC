
S = list(input())

K = int(input())

N = len(S)

ruiseki = [0] * (N+1)
M = 0
for i in range(N):
    if S[i] == '.':
        ruiseki[i+1] = ruiseki[i] + 1
    else:
        ruiseki[i+1] = ruiseki[i]


def is_ok(N,l,r,K,ruiseki):
    S = ruiseki[r+1] - ruiseki[l]
    if S <= K:
        return True

r = 0
ans = 0
for l in range(N):
    while r < N and is_ok(N,l,r,K,ruiseki):
        r = r + 1
    #print([l,r])
    ans = max([ans,r-l])

print(ans)
