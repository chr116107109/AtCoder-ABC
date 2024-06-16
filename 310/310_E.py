
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = input()

S = list(map(int,S))
d = [[0,0] for i in range(N)]
d[0][S[0]] += 1

ans = d[0][1]
for i in range(1,N):
    d[i][((0&S[i])+1)%2] += d[i-1][0]
    d[i][((1&S[i])+1)%2] += d[i-1][1]

    d[i][S[i]] += 1

    ans += d[i][1]

print(ans)