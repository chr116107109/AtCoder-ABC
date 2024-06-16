import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
A = list(map(int,input().split()))

x = max(A)
A.remove(x)
y = -1
for i in range(N-1):
    if abs(y-x//2) > abs(A[i]-x//2):
        y = A[i]
print(x,y)