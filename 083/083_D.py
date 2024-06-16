
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = [int(i) for i in list(input())]
N = len(S)
l = 1
r = N

while r < l:
    m = (r+l)//2
    d = [1] * (N+1)
    for i in range(N):
        d[i] *= d[i-1]
        if S[i]*d[i] == 1:
            d[i+1] *= -1
            d[min(N,i+m)] *= -1

            

