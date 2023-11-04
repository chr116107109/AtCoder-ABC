

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())
S = list(input())


l = 1
r = N + 1

def calc_n_block(T):
    n_block = 0
    now = T[0]
    if now == '0':
        n_block = 1
    for i in range(1,len(T)):
        if T[i] == now:
            continue
        elif T[i] == '0':
            n_block += 1
            now = T[i]
        else:
            now = T[i]
    
    return n_block


while l < r:
    m = (l+r)//2
    #print(l,r)
    is_ok = False
    T = deque((S[:m]))
    n_block = calc_n_block(T)
    if n_block <= K:
        is_ok = True

    for i in range(N-m):
        if T[0] != T[1] and T[0] == '0':
            n_block -= 1
        if T[-1] != S[i+m] and S[i+m] == '0':
            n_block += 1
        
        T.popleft()
        T.append(S[i+m])
        #print(T)
        #print(n_block)
        if n_block <= K:
            is_ok = True
            #break

    if is_ok:
        l = m + 1
    else:
        r = m

print(l-1)