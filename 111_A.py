
S = input()
ans = ''
for i in range(3):
    if S[i] == '1':
        ans += '9'
    else:
        ans += '1'
print(ans)