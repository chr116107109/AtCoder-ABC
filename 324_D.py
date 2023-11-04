import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
S = input()

ans = 0

for i in range(32*10**5):

    x = pow(i,2)

    S_count = {}
    for s in S:
        if s in S_count:
            S_count[s] += 1
        else:
            S_count[s] = 1

    ok = True
    for n in str(x):
        if not n in S_count or S_count[n] == 0:
            ok = False
            break
        S_count[n] -= 1
        
    if ok == False:
        continue
    #print(i)
    #print(S_count)
    #print(x_count)
    ok = True
    for n in S_count:
        if S_count[n] != 0:
            if n == '0':
                if S_count[n] >= 0:
                    continue
                else:
                    ok = False
                    break
            else:
                ok = False
                break
        
    if ok:
        ans += 1

print(ans)