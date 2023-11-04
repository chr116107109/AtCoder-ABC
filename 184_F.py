

N,T = map(int,input().split())
A = list(map(int,input().split()))
B = A[:N//2]
C = A[N//2:]

d1 = [{0} for i in range(len(B)+1)]
for i in range(1,len(B)+1):
    for b in d1[i-1]:
        d1[i].add(b)
        d1[i].add(b+B[i-1])

d2 = [{0} for i in range(len(C)+1)]
for i in range(1,len(C)+1):
    for b in d2[i-1]:
        d2[i].add(b)
        d2[i].add(b+C[i-1])

L = sorted(list(d1[-1]))
R = sorted(list(d2[-1]))

import bisect
ans = 0
for i in range(len(L)):
    j = bisect.bisect_left(R,T-L[i]+0.5)
    #print(L[i],R[j-1])
    if L[i]+R[j-1] <= T:
        ans = max(ans,L[i]+R[j-1])

print(ans)