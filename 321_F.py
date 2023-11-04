

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math



Q,K = map(int,input().split())


d = [[0] * (2*K+10)]
d[0][0] = 1

mod=998244353

ans = []
q = []
for i in range(Q):
    q.append(list(input().split()))

parent = [0] * Q
for i in range(Q):
    if q[i][0] == '+':
        x = q[i][1]
        for j in range(i+1,Q):
            if q[j][1] == x and q[j][0] == '+':
                break
            if q[j][1] == x and q[j][0] == '-':
                parent[i] = j
                break
        