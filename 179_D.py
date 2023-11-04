from collections import Counter

N,K = map(int,input().split())
d = [[0,Counter()] for i in range(N)]
P = 998244353
A = [list(map(int,input().split())) for i in range(K)]


d[0][0] = 1
for i in range(N):
    for key in d[i][1]:
        if key == 'L':
            d[i][0] += d[i][1]['L']
            d[i][0] %= P
            if i+1 < N:
                d[i+1][1]['L'] += d[i][1]['L']
        if key == 'R':
            d[i][0] -= d[i][1]['R']
            d[i][0] %= P
            if i+1 < N:
                d[i+1][1]['R'] += d[i][1]['R']
    for j in range(K):
        L,R = A[j]
        if i+L < N:
            d[i+L][1]['L'] += d[i][0]
        if i+R+1 < N:
            d[i+R+1][1]['R'] += d[i][0]

    #print(d)


print(d[-1][0])