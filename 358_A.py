import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S,T = map(str,input().split())

if S == "AtCoder" and T == "Land":
    print("Yes")
else:
    print("No")