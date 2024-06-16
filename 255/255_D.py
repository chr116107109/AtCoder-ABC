
import bisect

N,Q = map(int,input().split())
A = list(map(int,input().split()))
X = [int(input()) for i in range(Q)]

A.sort()
ruiseki = [0] * (N+1)
for i in range(1,N+1):
    ruiseki[i] = ruiseki[i-1] + A[i-1]

for i in range(Q):
    ind = bisect.bisect_left(A,X[i])
    ans = (X[i]*ind - ruiseki[ind]) + (ruiseki[N] - ruiseki[ind] - X[i]*(N-ind) )
    #print(ind)
    print(ans)