

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = list(map(int,input().split()))
a2n = [2,5,5,4,5,6,3,7,6]
d = [[] for i in range(N+1)]
d[0] = [[0,0]]

def is_less(a,b):
    l_a = sum([aa[1] for aa in a])
    l_b = sum([bb[1] for bb in b])
    if l_a != l_b:
        return l_a < l_b
    else:
        if a == b:
            return True
        for i in range(len(a)):
            x,n = a[i]
            y,m = b[i]
            if n == m and x == y:
                continue
            elif x != y:
                return x < y
            elif m < n:
                return x < b[i+1][0]
            else:
                return a[i+1][0] < y

import copy
for i in range(1,N+1):

    for a in A:
        a_n = a2n[a-1]
        if i >= a_n and d[i-a_n] != []:
            if d[i-a_n][-1][0] == a:
                new = copy.deepcopy(d[i-a_n])
                new[-1][1] += 1
            else:
                new = copy.deepcopy(d[i-a_n])
                new.append([a,1])
            if is_less(d[i],new):
                d[i] = copy.deepcopy(new)
        
    #print(d[i])


ans = []
for a in d[-1][1:]:
    ans.append(str(a[0])*a[1])
print("".join(ans))