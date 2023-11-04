
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))
S = input()
ans = 0
for x,y,z in itertools.product([0,1,2],repeat=3):
    d = [[0,0,0] for i in range(N+1)]
    for i in range(1,N+1):
        d[i][0] = d[i-1][0]
        d[i][1] = d[i-1][1]
        d[i][2] = d[i-1][2]
        if S[i-1] == 'M' and A[i-1] == x:
            d[i][0] += 1
        if S[i-1] == 'E' and A[i-1] == y:
            d[i][1] += d[i][0]
        if S[i-1] == 'X' and A[i-1] == z:
            d[i][2] += d[i][1]

    nokori = [0,1,2,3]
    if x in nokori:
        nokori.remove(x)
    if y in nokori:
        nokori.remove(y)
    if z in nokori:
        nokori.remove(z)
    
    ans += d[-1][-1]*min(nokori)

print(ans)