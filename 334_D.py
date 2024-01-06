import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,Q = map(int,input().split())

A = list(map(int,input().split()))
A.sort()
B = [0]
for i in range(N):
    B.append(B[-1] + A[i])

ans = []
for i in range(Q):
    q = int(input())
    idx = bisect_right(B,q)
    ans.append(max(idx-1,0))

print(*ans,sep="\n")