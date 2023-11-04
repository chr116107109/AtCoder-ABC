from heapq import heappush,heappop
N,M = map(int,input().split())
A = list(map(int,input().split()))

q = []
for i in range(N):
    heappush(q,-A[i])

for i in range(M):
    #print(q)
    a = heappop(q)
    heappush(q,(a+2-1)//2)

print(-sum(q))
