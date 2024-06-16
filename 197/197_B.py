


import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W,X,Y = map(int,input().split())
X -= 1
Y -= 1
S = []
for i in range(H):
    S.append(input())

ans = 1
for i in range(1,H):
    if X+i < H and S[X+i][Y] == '.':
        ans += 1
    else:
        break

for i in range(1,H):
    if X-i >= 0 and S[X-i][Y] == '.':
        ans += 1
    else:
        break

for i in range(1,W):
    if Y+i < W and S[X][Y+i] == '.':
        ans += 1
    else:
        break

for i in range(1,W):
    if Y-i >= 0 and S[X][Y-i] == '.':
        ans += 1
    else:
        break


print(ans)