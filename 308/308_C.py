import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
from decimal import Decimal

N = int(input())

A = [list(map(int,input().split())) for i in range(N)]

d = []

for i in range(N):
    d.append([(A[i][0]/(A[i][0]+A[i][1])),i])
d.sort(key=lambda x:-x[0]*10**10+x[1])

print(*[s[1]+1 for s in d])
