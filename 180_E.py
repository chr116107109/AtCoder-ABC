

N = int(input())
g = [[] for i in range(N)]
citi = []
for i in range(N):
    x,y,z = map(int,input().split())
    citi.append([x,y,z])

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        dist = abs(citi[i][0]-citi[j][0]) + abs(citi[i][1]-citi[j][1]) + max(0,citi[j][2]-citi[i][2])
        g[i].append([j,dist])

inf = 10**10
d = [[inf]*N for i in range(2**N)]

d[1][0] = 0

for i in range(2**N):
    for j in range(N):
        if i&(1<<j) == 0 and i > 0 and j > 0:
            continue

        for k,dist in g[j]:
            next = i|(1<<k)
            d[next][k] = min(d[next][k], d[i][j]+dist)

print(d[-1][0])