
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

ans1 = 0

now = 0
for i in range(N):
    now += A[i]
    if i%2 == 0:
        if now >= 0:
            ans1 += now+1
            now = -1

    if i%2 == 1:
        if now <= 0:
            ans1 -= now-1
            now = +1
    
        
ans2 = 0

now = 0
for i in range(N):
    now += A[i]
    if i%2 == 1:
        if now >= 0:
            ans2 += now+1
            now = -1
    if i%2 == 0:
        if now <= 0:
            ans2 -= now-1
            now = +1
    
    #print(ans2)

print(min(ans1,ans2))