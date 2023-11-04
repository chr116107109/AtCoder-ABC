import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(N):
    count = bisect_left(A,A[i]+M-0.5) - i 
    #print(A[i],count)
    ans = max(ans, count)

print(ans)