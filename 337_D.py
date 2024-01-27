import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W,K = map(int,input().split())   

S = [list(input()) for _ in range(H)]

ans = 10**10
for i in range(H):
    if W-K < 0:
        break
    d = Counter(S[i][:K])
    for j in range(W-K):
        if d['x'] == 0:
            ans = min(ans,d['.'])
        
        #print(d)
        d[S[i][j]] -= 1
        d[S[i][j+K]] += 1
        #print(d)
    if d['x'] == 0:
        ans = min(ans,d['.'])
# Sを転置
S = list(zip(*S))
H,W = W,H

for i in range(H):
    if W-K < 0:
        break
    
    d = Counter(S[i][:K])
    for j in range(W-K):
        if d['x'] == 0:
            ans = min(ans,d['.'])
        
        #print(d)
        d[S[i][j]] -= 1
        d[S[i][j+K]] += 1

    #print(d)
    if d['x'] == 0:
        ans = min(ans,d['.'])

if ans == 10**10:
    print(-1)
else:
    print(ans)
        


