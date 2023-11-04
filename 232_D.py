from collections import deque

[H,W] =  list(map(int,input().split()))

C = [input() for i in range(H)]


que = deque()
que.append([0,0])
d = [[-1] * W for i in range(H)]
d[0][0] = 1

ans = 1
while que:
    [x,y] = que.popleft()
    #print(que)

    if x < H-1 and y < W:
        if C[x+1][y] == '.':
            if [x+1,y] not in que:
                que.append([x+1,y])
            d[x+1][y] = d[x][y] + 1
            ans = max(ans,d[x+1][y])
    if y < W-1 and x < H:
        if C[x][y+1] == '.':
            if [x, y+1] not in que:
                que.append([x,y+1])
            d[x][y+1] = d[x][y] + 1
            ans = max(ans,d[x][y+1])

print(ans)
