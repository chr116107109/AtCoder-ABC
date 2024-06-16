import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
S = input()

if 'ab' in S or "ba" in S:
    print("Yes")
else:
    print("No")
