
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))
B = list(range(2**N))
while len(B) > 2:
    #print(A)
    next = []
    while B:
        a = B.pop()
        b = B.pop()
        if A[a] < A[b]:
            next.append(b)
        else:
            next.append(a)
    next.reverse()
    B = next[:]

a,b = B
if A[a] < A[b]:
    print(a+1)
else:
    print(b+1)