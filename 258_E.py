
from bisect import bisect_left
from itertools import accumulate


N,Q,X = map(int,input().split())
W = list(map(int,input().split()))
K = [int(input()) for i in range(Q)]

sumW = sum(W)
A = [0] + list(accumulate(W+W))

visited = {}
path = []
now = 0
while True:
    if now in visited:
        break
    path.append(now)
    Y = X%sumW
    next = (bisect_left(A,A[now+1]+Y-W[now]))
    n_poteto = N*(X//sumW)+(next-now)
    visited[now] = n_poteto
    now = next%N

n_before_loop = 0
n_loop = 0
i = 0
while now != path[i]:
    i += 1
n_before_loop = i
n_loop = len(path) - n_before_loop

for k in K:
    if k <= len(path):
        ans = visited[path[k-1]]
    else:
        k -= len(path)
        if n_loop != 1:
            k %= n_loop
        else:
            k = 1
        k = (k-1)%n_loop
        ans = visited[path[n_before_loop+k]]

    print(ans)
