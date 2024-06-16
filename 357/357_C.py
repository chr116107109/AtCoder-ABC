import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

from copy import deepcopy
N = int(input())

A = ['#']
B = deepcopy(A)
for i in range(N):
    B = [['.']*pow(3,i+1) for _ in range(pow(3,i+1))]

    for x in range(pow(3,i+1)):
        for y in range(pow(3,i+1)):
            if x//pow(3,i) == 1 and y//pow(3,i) == 1:
                continue
            B[x][y] = A[x%(pow(3,i))][y%(pow(3,i))]

    A = deepcopy(B)
for b in B:
    print(''.join(b))   