from collections import Counter
H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]

A.sort(key = lambda x:max(x))

g = [[set(),set()] for i in range(W+W)]

for i in range(H):
    a = {}
    for j in range(W):
        if A[i][j] in a:
            a[A[i][j]].append(j)
        else:
            a[A[i][j]] = [j]
    b = sorted(a.keys())
    for j in range(len(b)-1):
        g.append([set(),set()])
        if b[j] == 0:
            continue
        for s in a[b[j]]:
            g[s][0].add(W+j)
            g[W+j][1].add(s)
        for t in a[b[j+1]]:
            g[W+j][0].add(t)
            g[t][1].add(W+j)

from collections import deque
q = deque()
for i in range(len(g)):
    if g[i][1] == set():
        q.append(i)
l = []
#print(g)
while q:
    s = q.popleft()
    l.append(s)
    for t in g[s][0]:
        g[t][1].remove(s)
        if g[t][1] == set():
            q.append(t)

frag = 1

if len(l) < len(g):
    frag = 0
for i in range(H-1):
    if A[i+1] == [0] * W or A[i] == [0] * W:
        continue
    if max(A[i]) >= min([a for a in A[i+1] if a > 0]):
        frag = 0

if frag == 1:
    print('Yes')
else:
    print('No')