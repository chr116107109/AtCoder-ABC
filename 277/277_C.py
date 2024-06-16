
N = int(input())
g = {}

for i in range(N):
    A,B = map(int,input().split())
    if not A in g:
        g[A] = [B]
    else:
        g[A].append(B)

    if not B in g:
        g[B] = [A]
    else:
        g[B].append(A)

q = [1]
visited = set()

while q:
    s = q.pop()
    if s in visited:
        continue
    visited.add(s)
    if not s in g:
        continue
    for t in g[s]:
        q.append(t)

print(max(visited))