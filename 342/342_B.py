import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))
index = [0] * N
for i in range(N):
    index[A[i]-1] = i+1

Q = int(input())

for i in range(Q):
    a,b = map(int,input().split())
    if index[a-1] < index[b-1]:
        print(a)
    else:
        print(b)