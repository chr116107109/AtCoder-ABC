
N,M = map(int,input().split())

P = {}

for i in range(M):
    p,y = map(int,input().split())
    if p in P:
        P[p].append([y,i])
    else:
        P[p] = [[y,i]]


city = [''] * M

for p in P:
    c = P[p]
    c.sort(key=lambda x: x[0])

    sp = str(p)
    sp = '0'*(6-len(sp)) + sp
    for i in range(len(c)):
        sc = str(i+1)
        sc = '0'*(6-len(sc)) + sc
        #print(p,c[i][1])
        #print(sp,sc)
        city[c[i][1]] = sp+sc
        #print(city)

for c in city:
    print(c)