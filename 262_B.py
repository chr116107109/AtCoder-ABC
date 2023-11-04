
N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

import itertools

ans = 0
for i,j,k in itertools.combinations(range(N),3):
    [i,j,k] = sorted([i,j,k])
    if j in g[i] and k in g[j] and i in g[k]:
        ans += 1

print(ans)