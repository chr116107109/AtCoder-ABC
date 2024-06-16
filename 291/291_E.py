

N,M = map(int,input().split())

g = [[set(),set()] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1][0].add(b-1)
    g[b-1][1].add(a-1)

q = []

for i in range(N):
    if g[i][1] == set():
        q.append(i)

ans = [-1] * N 
now = 1
while q:
    if len(q) > 1:
        break

    s = q.pop()
    ans[s] = now
    for t in g[s][0]:
        g[t][1].remove(s)
        if g[t][1] == set():
            q.append(t)
    
    now += 1

if -1 in ans:
    print('No')
else:
    print('Yes')
    print(*ans)
