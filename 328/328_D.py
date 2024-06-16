import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


A = input()



ans_ind = []
def solve(i,s):
    print(i,s)
    if s == 'ABC':
        return i+1
    
    j = next
    solve(j,s+A[j])