
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = list(map(int,input().split()))

before = {M:0}
after = {M:0}

for i in range(N):
    #print(before)
    for s in before:
        if A[i] % s == 0:
            if s * A[i]//s in after:
                after[s * A[i]//s] +=  before[s]
            else:
                after[s * A[i]//s] = before[s]
        else:
            if M%(A[i] * s // math.gcd(A[i],s)) == 0:
                if A[i] * s // math.gcd(A[i],s) in after:
                    after[A[i] * s // math.gcd(A[i],s)] += before[s]
                else:
                    after[A[i] * s // math.gcd(A[i],s)] = before[s]


    if M%A[i] == 0:
        if A[i] in after:
            after[A[i]] += 1
        else:
            after[A[i]] = 1

    for a in after:
        before[a] = after[a]

print(after[M])