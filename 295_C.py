
N = int(input())
A = list(map(int,input().split()))

from collections import Counter

C = Counter()

for i in range(N):
    C[A[i]] += 1

ans = 0
for c in C:
    ans += C[c]//2

print(ans)