

N,C = map(int,input().split())

d = []
for i in range(N):
    s,t,c = map(int,input().split())
    d.append([s-0.5,c,'s'])
    d.append([t,c,'t'])

d.sort(key=lambda x:x[0])
ans = 1
count = 0
now = {}

for i in range(len(d)):
    if d[i][2] == 's':
        if not d[i][1] in now or now[d[i][1]] == 0:
            count += 1
            now[d[i][1]] = 1
        else:
            now[d[i][1]] += 1
    else:
        now[d[i][1]] -= 1
        if now[d[i][1]] == 0:
            count -= 1

    ans = max(ans,count)

print(ans)