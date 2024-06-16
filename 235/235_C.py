
[N,Q] = list(map(int,input().split()))

a = list(map(int,input().split()))

d = {}
for i in range(N):
    if a[i] in d.keys():
        d[a[i]] += [i]
    else:
        d[a[i]] = [i]


for i in range(Q):
    [x,k] = list(map(int,input().split()))

    if x in d.keys():
        if len(d[x]) >= k:
            print(d[x][k-1]+1)
        else:
            print(-1)
    else:
        print(-1)
