

import bisect

[N,Q] = list(map(int,input().split()))


A = list(map(int,input().split()))
A.sort()

for i in range(Q):
    x = int(input())
    print(N - bisect.bisect_left(A,x))
