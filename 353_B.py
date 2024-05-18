import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())

A = list(map(int,input().split()))

x = K
ans = 0
while A:
    a = A.pop(0)
    if x >= a:
        x -= a
    else:
        ans += 1
        x = K - a

print(ans+1)