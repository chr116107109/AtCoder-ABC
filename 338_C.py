import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B =  list(map(int,input().split()))

ans = 0

M = 10**6+10
for i in range(M):
    n_b = 10**6+10
    for j in range(N):
        if i*A[j] <= Q[j]:
            if B[j] > 0:    
                n_b = min(n_b,(Q[j]-i*A[j])//B[j])
        else:
            n_b = -1
            break

    if n_b == -1:
        continue
    #print(i,n_b)
    ans = max(ans,i+n_b)

print(ans)