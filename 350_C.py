import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

A = list(map(int,input().split()))  

pos = [-1] * N
for i in range(N):
    pos[A[i]-1] = i

ans = []

for i in range(N):
    #print(A)
    #print(pos)
    if i == pos[i]:
        continue
    ans.append((i+1, pos[i]+1))
    A[pos[i]], pos[A[i]-1] = A[i], pos[i]
    A[i], pos[i] = i+1, i

print(len(ans))
for a in ans:
    print(a[0],a[1])