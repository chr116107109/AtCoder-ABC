import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,L,R = map(int,input().split())

ans = list(range(1,N+1))

ans[L-1:R] = ans[L-1:R][::-1]

print(*ans) 