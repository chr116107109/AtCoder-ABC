
N,D,A = map(int,input().split())

from heapq import heappush,heappop

q = []
for i in range(N):
    x,h = map(int,input().split())
    heappush(q,[x,[0,h]])

power = 0
ans = 0
while q:
    #print(q,ans,power)
    x, s = heappop(q)
    if s[0] == 0:
        h = s[1]
        h -= power
        h = max(0,h)
        ans += -(-h//A)
        power += -(-h//A)*A
        heappush(q,[x+2*D+0.5,[1,-(-h//A)*A]])
    if s[0] == 1:
        power -= s[1]

print(ans)

