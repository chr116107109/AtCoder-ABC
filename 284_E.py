import sys
sys.setrecursionlimit(10**7)

N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

visited = set()
ans = 0 
def dfs(s):
    global ans
    if s in visited or ans > 10**6:
        return
    
    visited.add(s)
    ans += 1
    for t in g[s]:
        dfs(t)
    visited.remove(s)

dfs(0)
print(min(ans,10**6))