

K = int(input())

from heapq import heappush,heappop
q = []
for i in range(1,10):
    heappush(q,i)

count = 0

while q:
    count += 1
    #print(q)
    n = heappop(q)
    if count == K:
        print(n)
        break

    right_digit = n%10
    heappush(q,n*10+right_digit)
    if right_digit > 0:
        heappush(q,n*10+right_digit-1)
    if right_digit < 9:
        heappush(q,n*10+right_digit+1)

