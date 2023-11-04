
from curses import init_pair


Q = int(input())

from collections import deque
d = deque()
f = [0,0]
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x,c = q[1],q[2]
        d.append([c,x])
    if q[0] == 2:
        c = q[1]
        ans = 0
        while c > 0:
            #print(d)
            if f[0] <= c:
                ans += f[0]*f[1]
                c -= f[0]
                f[0] = 0
                if d:
                    f = d.popleft()
            else:
                ans += c*f[1]
                f[0] -= c
                c = 0
        print(ans)
