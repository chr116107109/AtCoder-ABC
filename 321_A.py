import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = list(input())

n = len(S)
ans = 'Yes'
for i in range(n-1):
    if S[i] <= S[i+1]:
        ans = 'No'

print(ans)