import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

ans = []
for i in range(len(S)):
    if not S[i] in "a, e, i, o, u":
        ans.append(S[i])

print("".join(ans))