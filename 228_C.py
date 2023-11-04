
[N,K] = list(map(int,input().split()))

P = [sum(list(map(int,input().split()))) for i in range(N)]

sortP = sorted(P,reverse= True)

border = sortP[K-1]


for i in range(N):
    if border - P[i] <= 300:
        print('Yes')
    else:
        print('No')
