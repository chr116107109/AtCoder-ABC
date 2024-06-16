import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            if i+j+k <= N:
                print(i,j,k)
        

