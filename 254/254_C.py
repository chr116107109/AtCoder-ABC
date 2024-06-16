
N,K = map(int,input().split())
a = list(map(int,input().split()))

modk = [[] for i in range(K)]
for i in range(N):
    modk[i%K].append(a[i])

for i in range(K):
    modk[i].sort()

frag = 1
for i in range(1,N):
    if modk[(i-1)%K][(i-1)//K] <= modk[(i)%K][(i)//K]:
        continue
    else:
        frag = 0

if frag == 1:
    print('Yes')
else:
    print('No')