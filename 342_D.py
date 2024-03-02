import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

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

A.sort()
zeros = A.count(0)
A = A[zeros:]
D = Counter()
for i in range(len(A)):
    a = A[i]
    p_set = set()
    while a > 1:
        if P[a] < 0:
            p = -P[a]
        else:
            p = P[a]
        count = 0
        while a%p == 0:
            a //= p
            count += 1

        if count%2 == 1:
            p_set.add(p)

    p_set_str = str(sorted(list(p_set)))
    D[p_set_str] += 1


ans = 0
for s in D:
    if D[s] > 1:
        ans += math.comb(D[s],2)


print(ans + zeros*(N-zeros) + zeros*(zeros-1)//2)

