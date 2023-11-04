
N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ruiseki = [0] * (M+1)
for i in range(1,M+1):
    ruiseki[i] = ruiseki[i-1] + B[i-1]

import bisect

time = 0
ans = 0
for i in range(N+1):
    n_book_a = i
    n_book_b = bisect.bisect(ruiseki,K-time)-1
    #print(n_book_a,n_book_b,time)
    if time <= K:
        ans = max(ans,n_book_a + n_book_b)
    if i < N:
        time += A[i]

print(ans)