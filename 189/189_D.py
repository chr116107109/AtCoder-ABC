
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = [input() for i in range(N)]

d = [[0,0] for i in range(N+1)]

d[0][0] = 1
d[0][1] = 1

for i in range(1,N+1): 
    if S[i-1] == 'AND':
        d[i][0] += d[i-1][0]
        d[i][1] += d[i-1][0] + 2*d[i-1][1]
    if S[i-1] == 'OR':
        d[i][0] += 2*d[i-1][0] + d[i-1][1]
        d[i][1] += d[i-1][1]

print(d[-1][0])