import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

ans = []

while True:
    n = int(input())
    ans.append(n)
    if n == 0:
        break

ans.reverse()
print(*ans,sep='\n')