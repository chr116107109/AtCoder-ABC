import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())

somen_q = []
for i in range(M):
    t,w,s = map(int,input().split())
    heappush(somen_q,[t,'somen',w,s])

hito_q = []
for i in range(N):
    heappush(hito_q,i)

ans = [0] * N

while somen_q:

    time, type, w, s = heappop(somen_q)
    if type == 'somen':
        if hito_q == []:
            continue
        hito = heappop(hito_q)
        ans[hito] += w
        heappush(somen_q, [time+s-0.5, 'hito', hito, hito])
    if type == 'hito':
        heappush(hito_q, w)

print(*ans,sep='\n')