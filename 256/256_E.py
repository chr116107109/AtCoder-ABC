
N = int(input())
X = list(map(int,input().split()))
C = list(map(int,input().split()))

g = [[] for i in range(N)]
g_rev = [[] for i in range(N)]
for i in range(N):
    g[X[i]-1].append([i,C[i]])
    g_rev[i].append([X[i]-1,C[i]])


from collections import deque

q = deque()
for i in range(N):
    if g[i] == []:
        q.append(i)

while q:
    s = q.popleft()
    for [t, cost] in g_rev[s]:
        g[t].remove([s,cost])
        if g[t] == []:
            q.append(t)

ans = 0
for i in range(N):
    start = i
    now = i
    cut = 10**20
    while True:
        if g[now] == []:
            break
        now, cost = g[now].pop()
        cut = min(cut,cost)
        if now == start: 
            break
    
    if cut < 10**20:
        ans += cut

print(ans)