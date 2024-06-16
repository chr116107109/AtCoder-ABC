import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

x = 0
y = 0
for i in range(N):
    a,b = map(int,input().split())
    x += a
    y += b


if x == y:
    print("Draw")
elif x > y:
    print("Takahashi")
else:
    print("Aoki")