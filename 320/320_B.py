import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


S = list(input())
N = len(S)
ans = 1
for i in range(N):
    for j in range(i+1,N):
        T = S[i:j+1]
        ok = True
        for k in range(len(T)//2):
            if T[k] != T[-k-1]:
                ok = False
        if ok:
            ans = max(ans,len(T))

print(ans)