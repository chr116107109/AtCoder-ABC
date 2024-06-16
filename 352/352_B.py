import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S  = input()
T = input()

i = 0
now = 0
ans = []
while i < len(S):
    if S[i] == T[now]:
        ans.append(now+1)
        now += 1
        i += 1
        if now == len(T):
            break
    else:
        now += 1

print(*ans)