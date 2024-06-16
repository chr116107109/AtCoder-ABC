import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,D = map(int,input().split())

S = [input() for i in range(N)]

ans = 0

for i in range(1,D+1):

    for j in range(D-i+1):
        ok = True
        for k in range(N):
            if S[k][j:j+i] != 'o'*i:
                ok = False
        
        if ok:
            ans = max(ans,i)

print(ans)