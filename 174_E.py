
N,K = map(int,input().split())

A = list(map(int,input().split()))

left = 1
right = max(A)

while abs(left - right) > 10**(-3):
    m = (left+right)/2

    count = 0
    for i in range(N):
        count += A[i]//m

    #print(m,count)
    if count <= K:
        right = m
    else:
        left = m

import math
print(math.ceil(left))