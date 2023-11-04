
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
        if nums[i] > 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = -i

    return nums

P = sieve_of_eratosthenes(10**5)

A = [0,0,0]
for i in range(3,10**5+1):
    if P[i] > 0 and P[(i+1)//2] > 0:
        A.append(A[-1]+1)
    else:
        A.append(A[-1])

Q = int(input())

for i in range(Q):
    l,r = map(int,input().split())
    print(A[r]-A[l-1])

