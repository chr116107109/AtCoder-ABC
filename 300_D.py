

N = int(input())

M = int(N**(1/2))

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

primes = sieve_of_eratosthenes(M)

ans = 0
for i in range(len(primes)):
    a = primes[i]
    if a > N**(1/5):
        break
    for j in range(i+1,len(primes)):
        b = primes[j]
        if primes[j] > (N/pow(a,2))**(1/3):
            break
        for k in range(j+1,len(primes)):
            c = primes[k]
            if primes[k] > (N/pow(a,2)/b)**(1/2):
                break
            if a*a*b*c*c <= N:
                ans += 1

print(ans)