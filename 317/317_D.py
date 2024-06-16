import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = [list(map(int,input().split())) for i in range(N)]

S = sum([a[2] for a in A])

inf = 10**20
before = [inf] * (S+1)
after = [inf] * (S+1)
before[0] = 0
for i in range(N):
    cost = max((A[i][1]-A[i][0])//2 + 1,0)
    value = A[i][2]
    for x in range(S+1):
        after[x] = min(after[x],before[x])
        if x + value <= S:
            after[x+value] = min(after[x+value], before[x] + cost)
            
    before = after[:]

ans = 10**20
for value in range(S//2+1,S+1):
    
    ans = min(ans,before[value])

print(ans)