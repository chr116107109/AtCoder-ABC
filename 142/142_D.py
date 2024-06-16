
from math import gcd

A,B = map(int,input().split())
g = gcd(A,B)

p = []
i = 2
M = g**(1/2)
while i <= M+1:
    if g%i == 0:
        p.append(i)
    while g%i == 0:
        g //= i
    i += 1
if g > 1:
    p.append(g)
print(len(p)+1)
