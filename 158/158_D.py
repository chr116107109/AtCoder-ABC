
S = list(input())
Q = int(input())

from collections import deque
d = deque(S)
dir = 1
for i in range(Q):
    q = list(input().split())
    q[0] = int(q[0])

    if q[0] == 1:
        dir += 1
        dir %= 2
    else:
        q[1] = int(q[1])
        f = q[1]
        c = q[2]
        if (f+dir)%2 == 0:
            d.appendleft(c)
        else:
            d.append(c)

ans = list(d)
if dir == 0:
    ans.reverse()
print(''.join(ans))