
N = int(input())

maxq = int((N//2)**(1/3))+1

import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime


# 素数の列挙
prime = sieve_of_eratosthenes(maxq)
primes = []
for p in range(maxq+1):
    if prime[p]:
        primes.append(p)

s = 0
t = len(primes)-1
ans = 0
before = [s,t]
while s < t:
    
    while primes[s]*primes[t]**3 <= N and s<t:
        s += 1
    
    #print(primes[s-1],primes[t])
    s -= 1
    #print(s,t)
    ans += s + 1
    s = max(0,s-2)
    t -= 1

print(ans)