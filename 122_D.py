
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

NG = {'AGC','ACG','GAC'}

def is_ok(s):
    if 'AGC' in s:
        return False
    t = s[1]+s[0]+s[2]+s[3]
    if 'AGC' in t:
        return False
    t = s[0]+s[1]+s[3]+s[2]
    if 'AGC' in t:
        return False
    t = s[0]+s[2]+s[1]+s[3]
    if 'AGC' in t:
        return False
    
    return True

d = [Counter() for i in range(N+1)]

d[0]['XXX'] = 1
mod = 10**9 + 7
for i in range(1,N+1):

    for bef in d[i-1]:
        for s in ['A','G','C','T']:
            if is_ok(bef + s):
                d[i][bef[-2:] + s] += d[i-1][bef]
                d[i][bef[-2:] + s] %= mod

ans = 0
for v in d[-1].values():
    ans += v
    ans %= mod

print(ans)