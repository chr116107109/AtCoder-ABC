import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

ans = ''

on = True
for i in range(len(S)):
    if on and S[i] != '|':
        ans += S[i]
    if (not on) and S[i] == '|':
        on = True
    elif on and S[i] == '|':
        on = False

print(ans)