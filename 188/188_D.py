



N,C = map(int,input().split())
abc = [list(map(int,input().split())) for i in range(N)]

start_and_end = set()
id_cost = {}

for i in range(N):
    [a,b,c] = abc[i]
    start_and_end.add(a)
    start_and_end.add(b)
    if a in id_cost:
        id_cost[a].add((i,c,'L')) 
    else:
        id_cost[a] = {(i,c,'L')}
    if b in id_cost:
        id_cost[b].add((i,c,'R')) 
    else:
        id_cost[b] = {(i,c,'R')}
    
start_and_end = sorted(list(start_and_end))

ans = 0
now_cost = 0
before_day = 0
for today in start_and_end:
    ans += min(C,now_cost) * (today - before_day - 1)

    before_day = today
    for (id,cost,LR) in id_cost[today]:
        if LR == 'L':
            now_cost += cost
    
    ans += min(C,now_cost)
    for (id,cost,LR) in id_cost[today]:
        if LR == 'R':
            now_cost -= cost
    

    #print( now_cost,ans)


print(ans)