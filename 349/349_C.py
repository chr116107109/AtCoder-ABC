import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


S = input()
T = input()
S = S.upper()
ans = "No"

target = T[0]
ind = 0
for i in range(len(S)):
    if S[i] == target:
        if ind == 2:
            ans = "Yes"
            break
        ind += 1
        target = T[ind]

if T[-1] == "X":
    target = T[0]
    ind = 0
    for i in range(len(S)):
        if S[i] == target:
            if ind == 1:
                ans = "Yes"
                break
            ind += 1
            target = T[ind]

print(ans)