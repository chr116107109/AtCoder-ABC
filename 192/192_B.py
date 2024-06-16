
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


S = input()

for i,s in enumerate(S):
    if (i % 2 == 0 and s.lower() == s) or (i % 2 == 1 and s.upper() == s):
        continue
    else:
        print('No')
        sys.exit()

print('Yes')
