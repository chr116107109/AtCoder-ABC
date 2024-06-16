import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

d = set()

for i in range(len(S)):
    for j in range(i+1,len(S)+1):
        d.add(S[i:j])

print(len(d))


