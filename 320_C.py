import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

M = int(input())

S1 = list(input())
S2 = list(input())
S3 = list(input())


ans = 10**10

for i,j,k in itertools.product(range(M),repeat=3):
    if S1[i] == S2[j] == S3[k]:
        score = max(i,j,k)
        if i == j == k:
            score += 2*M
        elif i == j:
            if i < k:
                score += (M-k) + i
            else:
                score += M
        elif i == k:
            if i < j:
                score += (M-j) + i
            else:
                score += M
        elif k == j:
            if j < i:
                score += (M-i) + j
            else:
                score += M
        
        #print(i,j,k)
        #print(score)
        ans = min(ans,score)

if ans == 10**10:
    print(-1)
else:
    print(ans)
