import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

M = 0
while 2**M < N:
    M += 1 

print(M)

d = [[] for i in range(M)]
for i in range(N):
    for j in range(M):
        if (1 << j) & i != 0:
            d[j].append(i+1)

for i in range(M):
    print(len(d[i]),*d[i])

S = input()

ans = set(range(N))
for i in range(M):
    if S[i] == '1':
        d[i] = set(d[i])
        for j in range(N):
            if not j+1 in d[i]:
                if j in ans:
                    ans.remove(j)
    else:
        d[i] = set(d[i])
        for j in range(N):
            if j+1 in d[i]:
                if j in ans:
                    ans.remove(j)

print(list(ans)[0]+1)