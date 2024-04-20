import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

d = Counter(S)
t = defaultdict(list)

for a,b in d.items():
    t[b].append(a)

ans = 'Yes'
for b in t:
    if len(t[b]) != 2:
        ans = 'No'
        break

print(ans)