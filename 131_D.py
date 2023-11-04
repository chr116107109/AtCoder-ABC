
N = int(input())

AB = [list(map(int,input().split())) for i in range(N)]

AB.sort(key = lambda x: x[1])

time = 0
frag = 0

for i in range(N):
    if AB[i][1] - time >= AB[i][0]:
        time += AB[i][0]
    else:
        frag = 1
        break

if frag == 1:
    print('No')
else:
    print('Yes')
