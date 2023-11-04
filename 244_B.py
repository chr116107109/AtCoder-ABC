
N = int(input())
T = input()

ans = [0,0]
dir = 0
for i in range(N):
    if T[i] == 'S':
        if dir == 0:
            ans[0] += 1
        if dir == 1:
            ans[1] -= 1
        if dir == 2:
            ans[0] -= 1
        if dir == 3:
            ans[1] += 1
    if T[i] == 'R':
        dir = (dir+1)%4


print(*ans)



