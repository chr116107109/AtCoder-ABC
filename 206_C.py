from collections import Counter

N = int(input())
A = list(map(int,input().split()))

C = Counter()

ans = 0
for i in range(N):
    ans += i - C[A[i]]
    C[A[i]] += 1
    
print(ans)