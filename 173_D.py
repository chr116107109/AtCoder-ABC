from heapq import heappush,heappop
from collections import deque
N = int(input())
A = list(map(int,input().split()))

A.sort()

q = deque()

ans = A.pop()
q.append(A[-1])
q.append(A[-1])
A.pop()
while A:
    #print(ans)
    #print(q)
    ans += q.popleft()
    q.append(A[-1])
    q.append(A[-1])
    A.pop()


print(ans)

