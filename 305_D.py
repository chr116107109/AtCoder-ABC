import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math



N = int(input())
A = list(map(int,input().split()))

B = [0] * (N+1)
for i in range(1,N+1):
    B[i] = B[i-1]
    if i%2 == 1:
        continue
    B[i] += A[i]-A[i-1]

Q = int(input())

out = []
for i in range(Q):
    l,r = map(int,input().split())

    l_ind = bisect_right(A,l)
    r_ind = bisect_left(A,r)

    ans = B[r_ind] - B[l_ind]

    if l_ind%2 == 0:
        ans += A[l_ind] - l
    if r_ind%2 == 0:
        ans -= A[r_ind] - r

    out.append(ans)

print(*out,sep='\n')