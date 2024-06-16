
import sys
sys.setrecursionlimit(10**6)


N = int(input())
g = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)
ans = [[0,0] for i in range(N)]
visited = set()
def dfs(g,now,num):
    if len(g[now]) == 1 and g[now][0] in visited:
        ans[now] = [num+1,num+1]
        return [num+1,num+1]
    L = N
    R = 0
    visited.add(now)
    for next in g[now]:
        if next in visited:
            continue
        l,r = dfs(g,next,num)
        L = min(L,l)
        R = max(R,r)
        num = max(num,R)
    ans[now] = [L,R]
    return [L,R]

num = 0
dfs(g,0,num)

for i in range(N):
    print(*ans[i])