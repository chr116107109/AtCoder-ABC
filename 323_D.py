

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

size2count = Counter()
q = []
for i in range(N):
    size2count[A[i][0]] += A[i][1]
    heappush(q,A[i][0])

ans = 0
while q:
    #print(q)
    #print(size2count)
    s = heappop(q)
    c = size2count[s]
    del size2count[s]
    if c%2 == 1:
        ans += 1
        c -= 1
    if c == 0:
        continue
    if not s*2 in size2count:
        heappush(q,s*2)
    size2count[s*2] += c//2

print(ans)