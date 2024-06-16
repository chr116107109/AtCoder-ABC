import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

S = []
C = 0
for i in range(N):
    s,c = input().split()
    c = int(c)
    S.append(s)
    C += c

S.sort()
print(S[C%N])