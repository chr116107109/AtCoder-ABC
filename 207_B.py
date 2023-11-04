import math

x = list(map(float, input().split()))

A = x[0]
B = x[1]
C = x[2]
D = x[3]

if D*C <= B:
    print(-1)
else:
    n = (A/(D*C-B))
    print(math.ceil(n))
