
from collections import Counter

[N,K] = list(map(int,input().split()))

A = list(map(int,input().split()))

comm = [0] * (N+1)
for i in range(1,N+1):
    comm[i] = comm[i-1] + A[i-1]

d = Counter()
ans = 0

for x in comm:
    y = x - K
    ans += d[y]
    d[x] += 1
    #print(x,y,d[y])

print(ans)