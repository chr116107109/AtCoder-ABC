

N,M = map(int,input().split())
g = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)

ng = set()
ans = 0
for i in range(N):
    #print(i,ng)
    if not i in ng:
        for s in g[i]:
            ng.add(s)        
    else:
        ans += 1
        ng = set()
        for s in g[i]:
            ng.add(s)        

print(ans)