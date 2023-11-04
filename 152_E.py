
N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7
import math

l = A[0]
for i in range(1,N):
    l *= (A[i]//math.gcd(l,A[i]))
    

ans = 0
for i in range(N):
    ans += (l*pow(A[i],-1,mod))%mod
    ans %= mod

print(ans)

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