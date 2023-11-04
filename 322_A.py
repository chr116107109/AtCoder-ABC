import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = input()

for i in range(N-2):
    if S[i:i+3] == 'ABC':
        print(i+1)
        sys.exit()

print(-1)