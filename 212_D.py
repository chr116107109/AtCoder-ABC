
Q = int(input())

from heapq import heappop, heappush
h = []
d = [0] * (Q+1)
pre = 0
for i in range(1,Q+1):
    p = list(map(int,input().split()))
    d[i] = d[i-1]
    if p[0] == 3:
        x,ind= heappop(h)
        x += d[i]
        print(x)
    if p[0] == 1:
        x = p[1] - d[i]
        heappush(h,(x,i))
    if p[0] == 2:
        x = p[1]
        d[i] += x
    #print(h)