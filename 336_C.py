import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

N = int(input())

n = base10int(N-1, 5)

a = ['0','2','4','6','8']

ans = [a[int(i)] for i in n]

print(''.join(ans))