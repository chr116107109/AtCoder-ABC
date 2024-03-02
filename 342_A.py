import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

c = Counter(S)

for a in c:
    if c[a] == 1:
        x = a

for i in range(len(S)):
    if S[i] == x:
        print(i+1)
        break
