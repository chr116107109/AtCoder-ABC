import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
d = [[100, []] for i in range(37)]
for i in range(N):
    C = int(input())
    A = list(map(int,input().split()))
    for a in A:
        if d[a][0] > C:
            d[a][1] = [i+1]
            d[a][0] = C
        elif d[a][0] == C:
            d[a][1].append(i+1)


X = int(input())

print(len(d[X][1]))
print(*d[X][1])