import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
S = input()

nokori_m = M
nokori_r = 0
ans = 0
for i in range(N):
    #print(nokori_m,nokori_r,ans)
    if S[i] == "0":
        nokori_m = M
        nokori_r = ans
    elif S[i] == "1":
        if nokori_m == 0 and nokori_r == 0:
            ans += 1
        elif nokori_m == 0:
            nokori_r -= 1
        else:
            nokori_m -= 1
    elif S[i] == "2":
        if nokori_r == 0:
            ans += 1
        else:
            nokori_r -= 1

print(ans)