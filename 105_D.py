
N,M = map(int,input().split())
A = list(map(int,input().split()))

from collections import Counter
C = Counter()
now = 0
for i in range(N):
    now += A[i]
    now %= M
    C[now] += 1
#print(C)
now = 0
ans = 0
for i in range(N):
    ans += C[now]
    now += A[i]
    now %= M
    C[now] -= 1

print(ans)