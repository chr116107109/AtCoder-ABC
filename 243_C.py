
N = int(input())
XY = [list(map(int,input().split())) + [i] for i in range(N)]
S = input()

M = 10**10
XY = sorted(XY, key=lambda x: M*x[1]+x[0])


frag = 0
now = XY[0]
for i in range(1,N):
    #print(now[0],now[1],S[now[2]])
    #print(XY[i][0],XY[i][1],S[XY[i][2]])
    if now[1] == XY[i][1]:
        if S[now[2]] == 'R' and S[XY[i][2]] == 'L':
            frag = 1
            break
        elif S[now[2]] == 'L' and S[XY[i][2]] == 'R':
            now = XY[i]
    
    else:
        now = XY[i]


if frag == 1:
    print('Yes')
else:
    print('No')