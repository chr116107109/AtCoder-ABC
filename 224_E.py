import operator
import sys
from collections import Counter,defaultdict
[H,W,N] = list(map(int,input().split()))

rca = [[i] + list(map(int,input().split())) for i in range(N)]

g = defaultdict(list)
V = set()
for i in range(N):
    g[rca[i][3]].append([rca[i][0],rca[i][1],rca[i][2]])
    V.add(rca[i][3])

V = sorted(list(V),key=lambda x:-x)
ans = [0] * N
d = Counter()

#print(g)
for v in V:
    pool = []
    while g[v]:
        ind,r,c = g[v].pop()

        ans[ind] = max(d[r],d[-c]) + 1
        pool.append([r,c,ans[ind]])
    for r,c,a in pool:
        d[r] = max(d[r],a)
        d[-c] = max(d[-c],a)

    #print(d)

for a in ans:
    print(a-1)