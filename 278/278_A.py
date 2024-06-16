
N,K = map(int,input().split())
A = list(map(int,input().split()))

from collections import deque

A = deque(A)
for i in range(K):
    A.popleft()
    A.append(0)

print(*A)