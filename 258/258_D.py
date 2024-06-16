
N,X = map(int,input().split())

AB = [list(map(int,input().split())) for i in range(N)]

ruiseki_AplusB = [0] * (N+1)
minB = [AB[0][1]] * (N + 1)

for i in range(1,N+1):
    ruiseki_AplusB[i] = ruiseki_AplusB[i-1] + (AB[i-1][0]+AB[i-1][1])

    minB[i] = min(minB[i-1],AB[i-1][1])

ans = 10**20

for i in range(1,N+1):
    zantei = ruiseki_AplusB[i]
    Y = X - i
    zantei += minB[i] * Y
    ans = min(ans,zantei)

print(ans)
