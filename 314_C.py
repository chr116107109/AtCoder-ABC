import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())
S = input()
C = list(map(int,input().split()))
c2p = [deque() for i in range(M)]

for i in range(N):
    c2p[C[i]-1].append(S[i])

for i in range(M):
    a = c2p[i].pop()
    c2p[i].appendleft(a)

#print(c2p)
ans = []
for i in range(N):
    ans.append(c2p[C[i]-1].popleft())

print("".join(ans))