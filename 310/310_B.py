
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,M = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]

ans = 'No'
for i,j in itertools.permutations(range(N),2):
    S = set(A[i][2:])

    is_in = True
    for a in A[j][2:]:
        if not a in S:
            is_in = False

    if (is_in):
        if A[i][0] < A[j][0]:
            ans = 'Yes'
            break
        if A[i][0] == A[j][0] and len(S) > A[j][1]:
            ans = "Yes"
            break

    

print(ans)