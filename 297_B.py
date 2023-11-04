

S = list(input())

before = -1
for i in range(8):
    if before == -1 and S[i] == 'B':
        before = i
    elif S[i] == 'B':
        after = i

ans = 'Yes'

if before%2 == after%2:
    ans = 'No'

before = -1
for i in range(8):
    if before == -1 and S[i] == 'R':
        before = i
    elif S[i] == 'R':
        after = i

if not before < S.index('K') < after:
    ans = 'No'

print(ans)