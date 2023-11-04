import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,X = map(int,input().split())
A = list(map(int,input().split()))

for i in range(0,101):
    B = A + [i]
    score = sum(B) - max(B) - min(B)
    if score >= X:
        print(i)
        sys.exit()

print(-1)