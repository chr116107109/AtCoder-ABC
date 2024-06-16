
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

C = set()

for i in range(N):
    S = input()
    T = S[-len(S)//2:]
    if S[:len(S)//2] > T[::-1]:
        S = S[::-1]

    C.add(S)

print(len(C))