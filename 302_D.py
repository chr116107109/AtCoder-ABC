
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right


N,M,D = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()
ans = -1
for i in range(N):
    k = bisect_left(B,A[i]+D)

    a = max(k-1,0)
    b = min(M-1,k)
    c = min(M-1,k+1)

    if abs(A[i]-B[b]) <= D:
        ans = max(ans,A[i]+B[b])
    if abs(A[i]-B[c]) <= D:
        ans = max(ans,A[i]+B[c])
    if abs(A[i]-B[c]) <= D:
        ans = max(ans,A[i]+B[c])

for i in range(M):
    k = bisect_left(A,B[i]+D)

    a = max(k-1,0)
    b = min(N-1,k)
    c = min(N-1,k+1)

    if abs(A[a]-B[i]) <= D:
        ans = max(ans,A[a]+B[i])
    if abs(A[b]-B[i]) <= D:
        ans = max(ans,A[b]+B[i])
    if abs(A[c]-B[i]) <= D:
        ans = max(ans,A[c]+B[i])
    

print(ans)