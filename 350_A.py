import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

a = int(S[3:])

if 1 <= a <= 315 or 317 <= a<= 349:
    print("Yes")
else:
    print("No")