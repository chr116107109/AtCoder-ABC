
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int,input().split()))

d = {}

for i in range(M):
    d[D[i]] = P[i+1]

ans = 0

for i in range(N):
    if C[i] in d:
        ans += d[C[i]]
    else:
        ans += P[0]

print(ans)