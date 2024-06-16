import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

binary = bin(N)[2:]
ans = 0
for i in range(len(binary)-1,-1,-1):
    if binary[i] == '0':
        ans += 1
    else:
        break

print(ans)