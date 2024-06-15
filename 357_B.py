import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

N = len(S)

count = 0
for i in range(N):
    is_upper = S[i].isupper()
    if is_upper:
        count += 1

if count > N//2:
    print(S.upper())
else:
    print(S.lower())