
N,M = map(int,input().split())
key = []
for i in range(M):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    key.append([a,c])

inf = 10**10
d = [inf] * (2**N)
d[0] = 0
for i in range(2**N):

    for j in range(M):
        cost, l = key[j]
        next = sum([2**(k-1) for k in l]) | i
        #print(i,next)
        d[next] = min(d[next], d[i]+cost)
        #print(d)

if d[-1] == inf:
    print(-1)
else:
    print(d[-1])