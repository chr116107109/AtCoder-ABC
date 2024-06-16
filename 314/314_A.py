import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

print(pi[:N+2])