

N,Q = map(int,input().split())

from heapq import heappush,heappop

M = 2*10**5
rate = [[] for i in range(M)]
members = [set() for i in range(M)]
clas = [0] * N
score = [0] *N

daihyo_rate = []
daihyo_mem = set()

for i in range(N):
    a,b = map(int,input().split())
    b -= 1
    heappush(rate[b],[-a,i])
    members[b].add(i)
    clas[i] = b
    score[i] = a

for i in range(M):
    if rate[i]:
        s, id = rate[i][0][0], rate[i][0][1]
        heappush(daihyo_rate,[-s,id])
        daihyo_mem.add(id)

ans = []
for i in range(Q):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    x = clas[c]
    clas[c] = d
    members[x].remove(c)
    if c in daihyo_mem:
        daihyo_mem.remove(c)
        while rate[x] and (not rate[x][0][1] in members[x]):
            heappop(rate[x])
        if rate[x]:
            s,id = rate[x][0][0], rate[x][0][1]
            daihyo_mem.add(id)
            heappush(daihyo_rate, [-s,id])


    members[d].add(c)
    emp = True
    if rate[d]:
        emp = False
        old_daihyo = rate[d][0][1]
    else:
        heappush(daihyo_rate, [score[c],c])
        daihyo_mem.add(c)
    heappush(rate[d],[-score[c],c])
    if rate[d][0][1] == c and not emp:
        heappush(daihyo_rate, [score[c],c])
        daihyo_mem.add(c)
        daihyo_mem.remove(old_daihyo)

    while not daihyo_rate[0][1] in daihyo_mem:
        heappop(daihyo_rate)
    
    #print(members)
    #print(rate)
    #print(daihyo_rate)
    #print(daihyo_mem)
    #print('')
    ans.append(daihyo_rate[0][0])

print(*ans,sep='\n')