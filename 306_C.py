

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

d = [[] for i in range(N)]

for i in range(3*N):
    d[A[i]-1].append(i+1)

ans = []
for i in range(N):
    ans.append([d[i][1],i+1])

ans.sort(key=lambda x:x[0])

print(*[a[1] for a in ans])