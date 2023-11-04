from collections import deque


N = int(input())
S = input()

A = [0] * N
B = deque([N])

S_rev = S[::-1]
for i in range(N):
    if S_rev[i] == 'L':
        B.append(N-i-1)

    if S_rev[i] == 'R':
        B.appendleft(N-i-1)


print(*list(B))