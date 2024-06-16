
N,W = map(int,input().split())

T = 2*10**5+10
d = [[] for i in range(T)]
for i in range(N):
    s,t,p = map(int,input().split())
    d[s].append(('s',p))
    d[t].append(('t',p))

ans = 'Yes'
now = 0
for i in range(T):
    for sign, p in d[i]:
        if sign == 's':
            now += p
        if sign == 't':
            now -= p
    #print(i,now)
    if now > W:
        ans = 'No'
        break

print(ans)