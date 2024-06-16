import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = [list(map(int,input().split())) for i in range(N)]

q_yet = []
for i in range(N):
    heappush(q_yet,A[i])
q_ok = []
now = 0

ans = 0
while q_yet or q_ok:
    #print(q_ok)
    #print(q_yet)
    #print(now,ans)
    if q_ok == []:
        a = heappop(q_yet)
        heappush(q_ok,a[0] + a[1])
        now = max(now,a[0])
    else:
        while q_yet and q_yet[0][0] <= now:
            b = heappop(q_yet)
            heappush(q_ok,b[0] + b[1])
        
        while q_ok and now > q_ok[0]:
            heappop(q_ok)
        if q_ok:
            heappop(q_ok)
            now += 1
            ans += 1

print(ans)