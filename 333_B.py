import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = list(input())
T = list(input())
S.sort()
T.sort()

def f(s):
    if abs(ord(s[1]) - ord(s[0])) == 1 or abs(ord(s[0]) - ord(s[1])) == 4:
        return 1
    if abs(ord(s[1]) - ord(s[0])) == 2 or abs(ord(s[0]) - ord(s[1])) == 3:
        return 2
    
if f(S) == f(T):
    print('Yes')
else:
    print('No')
    