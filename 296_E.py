
import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int,input().split()))

g = [[] for i in range(N)]
rg = [[] for i in range(N)]
for i in range(N):
    g[i].append(A[i]-1)
    rg[A[i]-1].append(i)

def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

label,group = scc(N,g,rg)

ans = set()
from collections import Counter
c = Counter(group)
for i in range(N):
    if i in g[i]:
        ans.add(A[i])
    if c[group[i]] > 1:
        ans.add(A[i])

print(len(ans))