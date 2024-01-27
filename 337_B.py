import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

ok = True

N = len(S)

count = 0
t = ''
while count < N:
    if S[count] == t:
        pass
    elif t == '' and (S[count] == 'A' or S[count] == 'B' or S[count] == 'C'): 
        t = S[count]
    elif t == 'A' and (S[count] == 'B' or S[count] == 'C'):
        t = S[count]
    elif t == 'B' and S[count] == 'C':
        t = 'C'
    else:
        ok = False
        break

    count += 1

if ok:
    print("Yes")    
else:
    print("No")