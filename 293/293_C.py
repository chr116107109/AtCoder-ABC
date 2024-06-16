
H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]

ans = 0
import itertools
for d in itertools.combinations(range(H+W-1),H-1):
    d = set(d)
    now = [0,0]
    visited = set()
    ok = True
    for j in range(H+W-1):
        if not 0<=now[0]<H or not 0<=now[1]<W:
            ok = False
            break
        if A[now[0]][now[1]] in visited:
            ok = False
            break
        visited.add(A[now[0]][now[1]])

        if j in d:
            now[0] += 1
        else:
            now[1] += 1
        
        #print(now,visited)
    
    if ok:
        #print(d)
        ans += 1

print(ans)