import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M,K = map(int,input().split())

A = [list(input().split()) for _ in range(M)]

ans = 0
for i in range(2**N):

    ok = True
    for k in range(M):
        cnt = 0
        C = int(A[k][0])
        a = list(map(int, A[k][1:C+1]))
        R = A[k][-1]
        for j in range(C):
            if i & (1 << (a[j]-1)) != 0:
                cnt += 1
        
        if (cnt >= K and R == 'o') or (cnt < K and R == 'x'):
            pass
        else:
            ok = False
            break
    
    if ok:
        ans += 1
        

print(ans)