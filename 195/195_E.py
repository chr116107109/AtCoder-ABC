
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = list(map(int,list(input())))
X = input()
d = [set() for i in range(N+1)]


d[-1] = {0}
for i in range(N-1,-1,-1):
    
    if X[i] == 'T':
        before = set()
        for j in range(7):
            if (j*10+S[i])%7 in d[i+1] or (j*10)%7 in d[i+1]:
                before.add(j)
        
    if X[i] == 'A':
        before = set()
        for j in range(7):
            if (j*10+S[i])%7 in d[i+1] and (j*10)%7 in d[i+1]:
                before.add(j)
    
    d[i] = before

if 0 in d[0]:
    print('Takahashi')
else:
    print('Aoki')

