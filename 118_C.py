
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = list(map(int,input().split()))

x = math.gcd(A[0],A[1])
for i in range(N):
    x = math.gcd(x,A[i])

print(x)