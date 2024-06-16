import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

S = [input() for i in range(N)]

ans=  10**10
for bit in range(2**N):
    a = ['x'] * M
    count = 0
    for i in range(N):
        if bit & (1<<i):
            continue
        count += 1
        for j in range(M):
            if S[i][j] == 'o':
                a[j] = 'o'
    
    if 'x' not in a:
        ans = min(ans,count)

print(ans)