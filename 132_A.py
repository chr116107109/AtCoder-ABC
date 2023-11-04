import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = list(input())
S.sort()
if len(set(S)) == 2 and S[0] == S[1] and S[2] == S[3]:
    print('Yes')
else:
    print('No')