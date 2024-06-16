

N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

from collections import Counter

ca = Counter(A)

ans = 0
for i in range(N):
    ans += ca[B[C[i]-1]]

print(ans)