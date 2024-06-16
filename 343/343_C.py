import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

ans = 0
for i in range(1,10**6+10):
    if i**3 > N:
        break
    

    s = str(i**3)
    ok = True
    for j in range(len(s)//2):
        if s[j] != s[-j-1]:
            ok = False
            break

    if ok:
        ans = max(ans,i**3)

print(ans)