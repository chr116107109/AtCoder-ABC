import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = list(input())

dmap = {}
for s in S:
    dmap[s] = s


Q = int(input())

for i in range(Q):
    c,d = input().split()
    
    for x in dmap:
        if dmap[x] == c:
            dmap[x] = d
    
    #print(dmap['s'])

for i in range(N):
    S[i] = dmap[S[i]]

print(''.join(S))