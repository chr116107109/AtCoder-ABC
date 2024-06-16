import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
from sys import exit

N = int(input())

x = 1
while True:
    if pow(x,x) == N:
        print(x)
        exit()
    elif  pow(x,x) > N:
        print(-1)
        exit()
    
    x += 1