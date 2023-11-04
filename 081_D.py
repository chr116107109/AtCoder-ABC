
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

ans = []
for i in range(N-1):
    if A[i+1] < A[i]:
        if A[i+1] < 0 < A[i]:
            ans.append([i,i+1])
            A[i+1] += A[i]
            ans.append([i,i+1])
            A[i+1] += A[i]
        elif A[i+1] < A[i] < 0:
            ans.append([i+1,i])
            A[i] += A[i+1]
        else:
            ans.append([i,i+1])
            A[i+1] += A[i]

print(len(ans))
for a in ans:
    print(*a)