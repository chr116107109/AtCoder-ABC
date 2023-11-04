
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

import math

def intsqrt(n):
    dig=0
    while pow(10,2*dig) < n:
        dig+=1
    
    sq=0
    for k in reversed(range(0,dig+1)):
        for l in range(0,10):
            sq+=10**k
            if sq*sq==n:
                break
            if sq*sq>n:
                sq-=10**k
                break
    return sq

p = sieve_of_eratosthenes(10**7)

T = int(input())

for i in range(T):
    N = int(input())
    for prime in p:
        if N%(prime*prime) == 0:
            print(prime,N//(prime*prime))
            break
        elif N%prime == 0:
            print(intsqrt(N//prime), prime)
            break




