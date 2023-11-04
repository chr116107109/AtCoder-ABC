
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
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


N = int(input())
P = sieve_of_eratosthenes(55555)

d = [[] for i in range(5)]

for p in P:
    d[p%5].append(p)

ans = []
for i in range(5):
    if len(d[i]) >= N:
        ans = d[i][:N]

if ans:
    print(*ans)
else:
    print(-1)