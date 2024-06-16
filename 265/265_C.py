
H,W = map(int,input().split())
A = [input() for i in range(H)]

visited = set()
now = [0,0]
import copy
while True:
    next = copy.deepcopy(now)
    #print(now)
    visited.add((now[0],now[1]))
    if A[now[0]][now[1]] == 'U' and now[0] > 0:
        next[0] -= 1
    if A[now[0]][now[1]] == 'D' and now[0] < H-1:
        next[0] += 1
    if A[now[0]][now[1]] == 'L' and now[1] > 0:
        next[1] -= 1
    if A[now[0]][now[1]] == 'R' and now[1] < W-1:
        next[1] += 1
    
    if next == now:
        ans = (now[0]+1, now[1]+1)
        print(*ans)
        break
    if (next[0],next[1]) in visited:
        ans = -1
        print(ans)
        break

    now = next

