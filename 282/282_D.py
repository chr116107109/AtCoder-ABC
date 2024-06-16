
from collections import deque
from itertools import accumulate


N,M = map(int,input().split())

g = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

def is_ok(s):
    q = deque()
    q.append([s,0])
    color = {}
    
    is_bin = True
    while q:
        s,c = q.popleft()
        if s in color:
            if color[s] != c:
                is_bin = False
            continue
        color[s] = c
        for t in g[s]:
            q.append([t,(c+1)%2])

    return is_bin, color

is_bin = True
D = []
visited = {}
for i in range(N):
    if i in visited:
        continue
    is_bin, color = is_ok(i)
    if is_bin:
        D.append(color)
    visited.update(color)
    if is_bin == False:
        break


ans = 0
for color in D:
    if is_bin == False:
        continue

    white = sum(color.values())
    black = len(color) - white
    for i,s in enumerate(color):
        if color[s] == 0:
            ans += white
        else:
            ans += black
        for t in g[s]:
            ans -= 1
        ans += N-len(color)

print(ans//2)