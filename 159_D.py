

N = int(input()) 
A = list(map(int,input().split()))

from collections import Counter
L = Counter()
R = Counter()
for i in range(N):
    R[A[i]] += 1

ans = 0
for r in R:
    if R[r] > 1:
        ans += R[r]*(R[r]-1)//2

for i in range(N):
    r = A[i]
    if R[r] > 1:
        ans -= R[r]*(R[r]-1)//2
        ans += (R[r]-1)*(R[r]-2)//2

    print(ans)

    if R[A[i]] > 1:
        ans += R[r]*(R[r]-1)//2
        ans -= (R[r]-1)*(R[r]-2)//2
    