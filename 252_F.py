import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,L = map(int,input().split())
A = list(map(int,input().split()))
q = []
for i in range(N):
    heappush(q,A[i])

if sum(A) < L:
    heappush(q,L-sum(A))
ans = 0
while len(q) > 1:
    #print(q)
    s = heappop(q)
    t = heappop(q)
    ans += s+t
    heappush(q,s+t)


print(ans)
