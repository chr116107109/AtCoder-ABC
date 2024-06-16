

N = int(input())
import math
def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

p = sieve_of_eratosthenes(N)

d = {}
one = 0
three = 0
five = 0
twfive = 0
sevfive = 0

for prime in p:
    i = 1
    count = 0
    while pow(prime,i) <= N:
        count += N//pow(prime,i)
        i += 1
    d[prime] = count

    if count >= 74:
        sevfive += count - 74
    if count >= 24:
        twfive += count - 24
    if count >= 4:
        five += count - 4
    if count >= 2:
        three += count - 2

ans = 0

import itertools

for prime in d:
    if d[prime] >= 74:
        ans += 1

for p1,p2 in itertools.combinations(p,2):
    if d[p1] >= 24 and d[p2] >= 2:
        ans += 1
    if d[p2] >= 24 and d[p1] >= 2:
        ans += 1
    if d[p1] >= 14 and d[p2] >= 4:
        ans += 1
    if d[p2] >= 14 and d[p1] >= 4:
        ans += 1
    
    
#print(ans)
for p1,p2,p3 in itertools.combinations(p,3):
    [a,b,c] = [d[p1],d[p2],d[p3]]
    if c>=4 and b>=4 and a>=2:
        ans += 1
    if a>=4 and b>=4 and c>=2:
        ans += 1
    if c>=4 and a>=4 and b>=2:
        ans += 1


print(ans)