import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,A,B = map(int,input().split())

D = list(map(int,input().split()))


C = set()
for i in range(N):
    C.add(D[i]%(A+B))
C = list(C)
C.sort()
ans = "No"

M = len(C)
if M == 1:
    ans = "Yes"
for i in range(M):
    if (C[(i+M-1)%(M)] - C[i])%(A+B) < A:
        ans = "Yes"
        break


print(ans)