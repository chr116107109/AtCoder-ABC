from heapq import heappush,heappop
N,M = map(int,input().split())

g = [[[],[]] for i in range(N)]

for i in range(M):
    A,B = map(int,input().split())
    g[A-1][0].append(B-1)
    g[B-1][1].append(A-1)

h = []
for i in range(N):
    if g[i][1] == []:
        heappush(h,i)

ans = []
while h:
    s = heappop(h)
    ans.append(s+1)
    for t in g[s][0]:
        g[t][1].remove(s)
        if g[t][1] == []:
            heappush(h,t)

if len(ans) < N:
    print(-1)
else:
    print(*ans)