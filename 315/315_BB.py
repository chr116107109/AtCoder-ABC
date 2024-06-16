import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

M = int(input())
A = list(map(int,input().split()))


x = (sum(A)+1)//2

now = 0
for i in range(M):
    now += A[i]
    if now >= x:
        print(i+1, A[i] - (now-x))
        break