
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())

S = input()

a = ['A','B','C']

for j,i in enumerate(S):
    if i in a:
        a.remove(i)
    
    if a == []:
        print(j+1)
        break