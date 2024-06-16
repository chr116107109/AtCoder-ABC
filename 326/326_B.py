import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

while True:
    S = str(N)
    if int(S[0])*int(S[1]) == int(S[2]):
        print(N)
        break
    N += 1