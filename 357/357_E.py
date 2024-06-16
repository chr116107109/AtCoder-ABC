import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
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

# 縮約後のグラフを構築
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

N = int(input())

A = list(map(int,input().split()))

g = [[] for i in range(N)]
rg = [[] for i in range(N)]
for i in range(N):
    a,b = i,A[i]-1
    g[a].append(b)
    rg[b].append(a)

label, group = scc(N, g, rg)
G0, GP = construct(N, g, label, group)


count = 0

q = []

rG = [set() for i in range(label)]  
    
for i in range(label):
    for j in G0[i]:
        rG[j].add(i)

for i in range(label):
    if len(G0[i]) == 0:
        q.append(i)


counts = [len(GP[i]) for i in range(label)] 

while q:
    #print(q)
    x = q.pop()
    count += counts[x] * len(GP[x])
    for y in rG[x]:
        counts[y] += counts[x]
        G0[y].remove(x)
        if len(G0[y]) == 0:
            q.append(y)

print(count)