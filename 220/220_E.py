

N,D = map(int,input().split())

mod=998244353

ans = 0
now = 0
for i in range(N-1):
    #print(i,ans)
    if 2*(N-now-1) - D + 1 < 0:
        continue
    elif now+D <= N-1:
        if D == 1:
            ans += ((pow(2,D+1,mod) + 2*(pow(2,mod-2,mod) * (D-1))) * pow(2,now,mod))%mod
        else:
            ans += ((pow(2,D+1,mod) + 2*(pow(2,D-2,mod) * (D-1))) * pow(2,now,mod))%mod
        ans %= mod
    elif D > 0:
        ans += (pow(2,D-1,mod) * (2*(N-now-1) - D + 1) * pow(2,now,mod))%mod
        ans %= mod
    now += 1
print(ans)


from collections import deque
def bfs(s,g):
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in g[s]:
            q.append((t,d+1))
    return visited


def gutyoku(N,M):
    g = [[]]
    now = 0
    for i in range(N-1):
        for j in range(2**i):
            g[now].append(len(g))
            g[now].append(len(g)+1)
            g.append([now])
            g.append([now])
            now += 1

    #print(g)
    dist = []
    for i in range(len(g)):
        dist.append(bfs(i,g))
    
    ans = 0
    for i in range(len(g)):
        for j in range(len(g)):
            if j in dist[i] and dist[i][j] == M:
                ans += 1
    
    return ans#,dist

#ans = gutyoku(N,D)
#print(ans)