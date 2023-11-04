from heapq import heappush,heappop

N,M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

A.sort(key=lambda x:-x[0])

now = 1
ans = 0
q = []
while now <= M:

    if A:
        while now == A[-1][0]:
            a = A.pop()
            heappush(q,-a[1])
            if not A:
                break
    #print(q)    
    if q:
        ans += -heappop(q)

    now += 1

print(ans)