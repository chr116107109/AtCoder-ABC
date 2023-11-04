
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = list(input())
T = list(input())

s_c = Counter(S).values()
t_c = Counter(T).values()

if set(s_c) == set(t_c):
    print('Yes')
else:
    print('No')


