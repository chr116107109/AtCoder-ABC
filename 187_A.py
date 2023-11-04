

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = input().split()

if sum(list(map(int,list(N)))) < sum(list(map(int,list(M)))):
    print(sum(list(map(int,list(M)))))
else:
    print(sum(list(map(int,list(N)))))

