

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

inds = [0] * N

g = [set() for i in range(N)]
ans = 0
player = set(range(N))
for i in player:
    a,b = i, A[i][inds[i]]-1
    g[a].add(b)
next = list(range(N))
while player:
    ans += 1
    
    count = 0
    macth = set()
    for i in next:
        for j in g[i]:
            if i in g[j]:
                macth.add((min(i,j),max(i,j)))
                count += 1
    #print(g)
    #print(macth)
    next = []
    for i,j in macth:
        g[i].remove(j)
        g[j].remove(i)
        inds[i] += 1
        inds[j] += 1
        if inds[i] == N-1:
            player.remove(i)
        else:
            g[i].add(A[i][inds[i]]-1)
            next.append(i)
        if inds[j] == N-1:
            player.remove(j)
        else:
            g[j].add(A[j][inds[j]]-1)
            next.append(j)

    if count == 0:
        ans = -1
        break


print(ans)    
