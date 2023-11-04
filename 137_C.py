

N = int(input())

d = {}
ans = 0
for i in range(N):
    S = list(input())
    S.sort()
    S = "".join(S)
    if S in d:
        ans += d[S]
        d[S] += 1
    else:
        d[S] = 1

print(ans)