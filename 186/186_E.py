

T = int(input())

# Euclidean Algorithm
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

# Euclidean Algorithm (non-recursive)
def gcd2(m, n):
    while n:
        m, n = n, m % n
    return m

# Extended Euclidean Algorithm
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

# lcm (least common multiple)
def lcm(m, n):
    return m//gcd(m, n)*n

import math
def solve(N,S,K):
    d,x,y = extgcd(N,K)
    if S%d != 0:
        return -1
    #print(d,x,y)
    N //= d
    S //= d
    return (-y)*(S)%N

ans = []
for i in range(T):
    N,S,K= map(int,input().split())
    ans.append(solve(N,S,K))

print(*ans,sep='\n')