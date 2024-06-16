
xy = [list(map(int,input().split())) for i in range(3)]

ans = [0,0]
if xy[0][0] == xy[1][0]:
    ans[0] = xy[2][0]
if xy[0][0] == xy[2][0]:
    ans[0] = xy[1][0]
if xy[1][0] == xy[2][0]:
    ans[0] = xy[0][0]

if xy[0][1] == xy[1][1]:
    ans[1] = xy[2][1]
if xy[0][1] == xy[2][1]:
    ans[1] = xy[1][1]
if xy[1][1] == xy[2][1]:
    ans[1] = xy[0][1]

print(*ans)