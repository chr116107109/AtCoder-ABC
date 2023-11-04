import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

if len(A) > 1:
    print(max(max(A[1:])-A[0]+1,0))
else:
    print(0)