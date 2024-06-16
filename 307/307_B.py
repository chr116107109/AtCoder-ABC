import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = [input() for i in range(N)]

ans = 'No'
for i,j in itertools.combinations(range(N),2):
    s,t = S[i],S[j]
    u = s+t
    is_ok = True
    for k in range(len(u)//2):
        if u[k] != u[len(u)-k-1]:
            is_ok = False

    if is_ok:
        ans = 'Yes'
        break

    s,t = S[j],S[i]
    u = s+t
    is_ok = True
    for k in range(len(u)//2):
        if u[k] != u[len(u)-k-1]:
            is_ok = False

    if is_ok:
        ans = 'Yes'
        break

print(ans)