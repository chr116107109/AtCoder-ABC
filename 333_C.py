import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = [int('1'*i) for i in range(1,30)]

ans = set()

for a,b,c in itertools.product(A,repeat=3):
    
    ans.add(a+b+c)


ans = sorted(list(ans))

print(ans[N-1])