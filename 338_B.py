import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

C = Counter(S)

ans = ('',0)

for t in C:
    if ans[1] < C[t]:
        ans = (t,C[t])
    elif ans[1] == C[t]:
        ans = (min(ans[0],t),C[t])

print(ans[0])