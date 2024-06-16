
S = input()
S = list(S)
ans = 0
while S:
    if S[-1] == '0' and S[-2] == '0':
        S.pop()
        S.pop()
        ans += 1
    else:
        S.pop()
        ans += 1

print(ans)