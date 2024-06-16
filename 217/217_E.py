from email import header
from heapq import heappop,heappush
from collections import deque
Q = int(input())

h = []
A = deque()
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        A.append(q[1])
    if q[0] == 2:
        if h == []:
            print(A.popleft())
        else:
            print(heappop(h))
    if q[0] == 3:
        while A:
            heappush(h,A.popleft())

