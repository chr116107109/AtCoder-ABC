

N = int(input())
S = input()

visited = set()
now = [0,0]

ans = 'No'
for i in range(N):
    if tuple(now) in visited:
        ans = 'Yes'
        break
    visited.add(tuple(now))
    if S[i] == 'R':
        now[0] += 1
    if S[i] == 'L':
        now[0] -= 1
    if S[i] == 'U':
        now[1] += 1
    if S[i] == 'D':
        now[1] -= 1

if tuple(now) in visited:
    ans = 'Yes'

print(ans)