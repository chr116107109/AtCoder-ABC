

N = int(input())
A = list(map(int,input().split()))

d = {}
for i in range(N):
    if A[i] in d:
        d[A[i]].append(i+1)
    else:
        d[A[i]] = [i+1]

import bisect
Q = int(input())
for i in range(Q):
    L,R,X = map(int,input().split())
    if X in d:
        l = bisect.bisect_left(d[X],L)
        r = bisect.bisect_right(d[X],R)
        print(r-l)
    else:
        print(0)
