
from re import M


[N,K] = list(map(int,input().split()))
A = list(map(int,input().split()))
A.sort()

l = 0
r = 10**20

while l < r:
    s = 0
    m = (l+r)//2
    for i in range(N):
        s += min(m,A[i])

    if s < m*K:
        r = m
    else:
        l = m+1

print(l-1)