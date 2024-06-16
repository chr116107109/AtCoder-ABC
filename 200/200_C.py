
N = int(input())
A = list(map(int,input().split()))

from collections import Counter

d = Counter()

for i in range(N):
    d[A[i]%200] += 1

ans = 0
for i in d:
    ans += d[i]*max(d[i]-1,0)//2

print(ans)