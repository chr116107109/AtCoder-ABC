
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

q = deque()
q.append(3)
q.append(5)
q.append(7)
visited = set()
ans = 0
while q:
    s = q.popleft()
    if s in visited or s > N:
        continue
    visited.add(s)
    a = str(s)
    if '3' in a and '5' in a and '7' in a:
        ans += 1

    q.append(10*s+3)
    q.append(10*s+7)
    q.append(10*s+5)

print(ans)