
N, Q = map(int, input().split())

x_valu = list(range(N))
x_basho = list(range(N))

for i in range(Q):
    x = int(input())-1

    basho = x_basho[x]
    #print(x_valu)
    #print(x_basho)

    if basho < N-1:
        x_valu[basho],x_valu[basho+1] = x_valu[basho+1],x_valu[basho]
        x_basho[x], x_basho[x_valu[basho]] = x_basho[x_valu[basho]], x_basho[x]
    elif basho == N-1:
        x_valu[basho],x_valu[basho-1] = x_valu[basho-1],x_valu[basho]
        x_basho[x], x_basho[x_valu[basho]] = x_basho[x_valu[basho]], x_basho[x]

for i in range(N):
    x_valu[i] += 1

print(*x_valu)
