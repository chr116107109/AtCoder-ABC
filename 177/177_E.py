
N = int(input())
A = list(map(int,input().split()))

from collections import Counter

def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] > 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = -i

    return nums

P = sieve_of_eratosthenes(max(A))
p_set = set()

is_pc = True

for i in range(N):
    a = A[i]
    while a > 1:
        if P[a] < 0:
            p = -P[a]
        else:
            p = P[a]
        while a%p == 0:
            a //= p
        #print(p,is_pc)
        if p in p_set:
            is_pc = False
        else:
            p_set.add(p)


import math
g = A[0]
for i in range(1,N):
    g = math.gcd(g,A[i])

if is_pc:
    print('pairwise coprime')
elif g == 1:
    print('setwise coprime')
else:
    print('not coprime')