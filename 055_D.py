

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = input()

d1 = [0] * N
d2 = [0] * N
d2[0] = 1
d3 = [0] * N
d3[-1] = 1
d4 = [0] * N
d4[0] = 1
d4[-1] = 1

def make(d):
    for i in range(N-2):
        if (S[i] == 'o' and d[i] == 0) or (S[i] == 'x' and d[i] == 1):
            d[i+1] = d[i-1]
        else:
            d[i+1] = (d[i-1]+1)%2

def check(d):
    res = True
    for i in range(N):
        if S[i] == 'o':
            if d[i] == 0 and d[i-1] != d[(i+1)%N]:
                res = False
            if d[i] == 1 and d[i-1] == d[(i+1)%N]:
                res = False
        if S[i] == 'x':
            if d[i] == 1 and d[i-1] != d[(i+1)%N]:
                res = False
            if d[i] == 0 and d[i-1] == d[(i+1)%N]:
                res = False
        
    return res

make(d1)
make(d2)
make(d3)
make(d4)

for d in [d1,d2,d3,d4]:
    if check(d):
        ans = []
        for i in range(N):
            if d[i] == 0:
                ans.append('S')
            else:
                ans.append('W')
        print("".join(ans))
        sys.exit()

print(-1)

