
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = list(input())
ans = len(N)
for i in range(1,2**len(N)):
    s = ''
    for j in range(len(N)):
        if i & (1<<j) != 0:
            s += N[j]
    
    s = int(s)
    if s % 3 == 0:
        ans = min(ans,len(N) - len(str(s)))

if ans == len(N):
    print(-1)
else:
    print(ans)


