
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())

a = N
for i in range(K):
    A = list(str(a))

    B = sorted(A)
    B = int("".join(B))
    C = sorted(A,reverse=True)
    C = int("".join(C))

    a = C-B

print(a)