

[N,D] = list(map(int,input().split()))


RL = [[0,0] for i in range(N)]


for i in range(N):
    loc = list(map(int,input().split()))
    RL[i][0] = loc[1]
    RL[i][1] = loc[0]

RL.sort()

x = RL[0][0]
count = 1
for i in range(1,N):
    if RL[i][1] <= x + D - 1:
        continue
    else:
        x = RL[i][0]
        count += 1

print(count)
