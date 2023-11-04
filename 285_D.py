

N = int(input())
g = [[[],[]] for i in range(N)]
StoInd = {}
TT = []
for i in range(N):
    S,T = input().split()
    StoInd[S] = i
    TT.append(T)

for i in range(N):
    T = TT[i]
    if T in StoInd:
        g[i][1].append(StoInd[T])
        g[StoInd[T]][0].append(i)

q = []
for i in range(N):
    if g[i][1] == []:
        q.append(i)

visited = set()
while q:
    s = q.pop()
    visited.add(s)
    for t in g[s][0]:
        g[t][1].remove(s)
        if g[t][1] == []:
            q.append(t)

if len(visited) == N:
    print('Yes')
else:
    print('No')