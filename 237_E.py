
from collections import deque
from heapq import heappop, heappush


[N,M] = list(map(int,input().split()))
H = list(map(int,input().split()))

d = [[] for i in range(N)]

for i in range(M):
    [u,v] = list(map(int,input().split()))
    d[u-1] += [v-1]
    d[v-1] += [u-1]

inf = 1 * 10**12
dist = [inf] * N
dist[0] = -H[0]

Q = [0]
def fun(x,y,H):
    if H[x] >= H[y]:
        return 0
    elif H[x] < H[y]:
        return -(H[x] - H[y])


while len(Q) > 0:
    x = heappop(Q)

    if dist[x] < H[x]:
        continue
    for y in d[x]:
        if dist[y] > dist[x] + fun(x,y,H):
            dist[y] = dist[x] + fun(x,y,H)
            heappush(Q,y)

print(max(-dist[i]-H[i] for i in range(N)))