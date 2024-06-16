import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,S,K = map(int,input().split())  
ans = 0
for i in range(N):
    a,b = map(int,input().split())
    ans += a*b

if ans >= S:
    print(ans)
else:
    print(ans+K)