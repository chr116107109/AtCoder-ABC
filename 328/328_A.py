import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,X = map(int,input().split())
A = list(map(int,input().split()))

print(sum(A[i] for i in range(N) if A[i] <= X))