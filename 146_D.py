
N = int(input())
g = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].append((b-1, i))
    g[b-1].append((a-1, i))

from collections import deque

q = deque()
q.append((0,0))
visited = set()
ans = [0] * (N-1)
while q:
    s,c = q.popleft()

    if s in visited:
        continue
    visited.add(s)

    incre = 1
    for [t, ind] in (g[s]):
        if t in visited:
            continue
        if incre == c:
            incre += 1
        q.append((t,incre))
        ans[ind] = incre
        incre += 1

print(max(ans))
for a in ans:
    print(a)