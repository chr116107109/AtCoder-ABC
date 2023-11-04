

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
A = list(map(int,input().split()))

d = Counter()
d[0] += 1
now_sum = 0
now_xor = 0
ans = 0
for i in range(N):
    for j in range(i,N):
        s_sum = 0
        s_xor = 0
        for k in range(i,j+1):
            s_sum += A[k]
            s_xor ^= A[k]

        if s_xor == s_sum:
            print(i,j)
            ans += 1


l,r = 0,0